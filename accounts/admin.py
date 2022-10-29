from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts,UserProfile
from django.utils.html import format_html

# Register your models here
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
     
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','city','state','country')
     
     
# class UserAddressBookAdmin(admin.ModelAdmin):
    # list_display = ('user','address','status')
    
    
admin.site.register(Accounts,AccountAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
# admin.site.register(UserAddressBook, UserAddressBookAdmin)