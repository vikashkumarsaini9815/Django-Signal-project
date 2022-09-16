from django.contrib import admin

# Register your models here.
from .models import User, User_profile

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','user_name','mobile']
admin.site.register(User,UserAdmin)


class User_profile_Admin(admin.ModelAdmin):
    list_display = ['id','city']
admin.site.register(User_profile,User_profile_Admin)