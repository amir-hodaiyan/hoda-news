from django.utils.translation import gettext_lazy as _
from django.core.exceptions import PermissionDenied
from django.template.response import TemplateResponse
from django.utils.html import format_html
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, reverse

from django_otp.conf import settings
from .models import TOTPDevice


@admin.register(TOTPDevice)
class TOTPDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~django_otp.plugins.otp_totp.models.TOTPDevice`.
    """
    list_display = ['user', 'name', 'confirmed']
    raw_id_fields = ['user']
    readonly_fields = ['qrcode_link', 'throttling_failure_timestamp', 'throttling_failure_count']
    radio_fields = {'digits': admin.HORIZONTAL}

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if not settings.OTP_ADMIN_HIDE_SENSITIVE_DATA:
            list_display = [*list_display, 'qrcode_link']
        return list_display

    def get_fieldsets(self, request, obj=None):
        # Show the key value only for adding new objects or when sensitive data
        # is not hidden.
        if settings.OTP_ADMIN_HIDE_SENSITIVE_DATA and obj:
            configuration_fields = ['step', 'digits', 'tolerance']
        else:
            configuration_fields = ['key', 'step', 'digits', 'tolerance', 'drift']
        fieldsets = [
            (_('Identity'), {
                'fields': ['user', 'name', 'confirmed'],
            }),
            (_('Configuration'), {
                'fields': configuration_fields,
            }),
            (_('Failed login'), {
                'fields': ['throttling_failure_timestamp', 'throttling_failure_count'],
            }),
        ]
        # Show the QR code link only for existing objects when sensitive data
        # is not hidden.
        if not settings.OTP_ADMIN_HIDE_SENSITIVE_DATA and obj:
            fieldsets.append(
                (None, {
                    'fields': ['qrcode_link'],
                }),
            )
        return fieldsets

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('user')
        return queryset

    def qrcode_link(self, device):
        try:
            href = reverse('admin:otp_totp_totpdevice_config', kwargs={'pk': device.pk})
            text = _('Visit')
            link = format_html(f'<a href="{href}">{text}</a>')
        except Exception:
            link = ''

        return link

    qrcode_link.short_description = _('Qrcode')

    def get_urls(self):
        urls = [
                   path('<int:pk>/config/', self.admin_site.admin_view(self.config_view),
                        name='otp_totp_totpdevice_config'),
                   path('<int:pk>/qrcode/', self.admin_site.admin_view(self.qrcode_view),
                        name='otp_totp_totpdevice_qrcode'),
               ] + super().get_urls()

        return urls

    def config_view(self, request, pk):
        if settings.OTP_ADMIN_HIDE_SENSITIVE_DATA:
            raise PermissionDenied()

        device = TOTPDevice.objects.get(pk=pk)
        if not self.has_view_or_change_permission(request, device):
            raise PermissionDenied()

        context = dict(
            self.admin_site.each_context(request),
            device=device,
        )

        return TemplateResponse(request, 'otp_totp/admin/config.html', context)

    def qrcode_view(self, request, pk):
        if settings.OTP_ADMIN_HIDE_SENSITIVE_DATA:
            raise PermissionDenied()

        device = TOTPDevice.objects.get(pk=pk)
        if not self.has_view_or_change_permission(request, device):
            raise PermissionDenied()

        try:
            import qrcode
            import qrcode.image.svg

            img = qrcode.make(device.config_url, image_factory=qrcode.image.svg.SvgImage)
            response = HttpResponse(content_type='image/svg+xml')
            img.save(response)
        except ImportError:
            response = HttpResponse('', status=503)

        return response
