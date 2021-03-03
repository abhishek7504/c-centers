from django.contrib import admin
from accounts.models import *

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['password']

admin.site.register(User,UserAdmin)
