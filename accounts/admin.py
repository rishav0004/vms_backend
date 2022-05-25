from django.contrib import admin

from .models import  CustomUser, Driver, Head, Vehicle, Manager
from django.contrib.auth.admin import UserAdmin

# class UserModel(UserAdmin):
#     list_display =  ['first_name','user_type']

admin.site.register(CustomUser)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Manager)
admin.site.register(Head)