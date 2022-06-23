from django.contrib import admin

from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email',  'reviewed']
    search_fields = ['email', 'subject', 'massage']
    list_filter = ['reviewed', 'created']
    list_per_page = 50

