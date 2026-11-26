from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ['email','first_name','last_name','is_active','username','last_login','data_joined']
    list_display_links = ['email','first_name','last_name']
    readonly_fields = ['last_login','data_joined']
    ordering = ['-data_joined']
    list_filter = ['is_active','is_staff','is_superadmin']
    search_fields = ['email','first_name','last_name','username']
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)
