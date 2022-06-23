from django.contrib import admin

from .models import EmployeesModel


@admin.register(EmployeesModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'thumbnail', 'rol', 'counter']
    list_filter = ['rol']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['counter']

    def get_fieldsets(self, request, obj=None):
        not_lang_code = 'fa'
        if request.LANGUAGE_CODE == 'fa':
            not_lang_code = 'en'

        list_generic_config = (
            'first_name', f'first_name_{not_lang_code}', 'last_name', f'last_name_{not_lang_code}', 'bio',
            f'bio_{not_lang_code}', 'profile_photo', 'membership_date', 'rol', 'counter')
        fieldsets = ((None, {'fields': list_generic_config}),)
        return fieldsets
