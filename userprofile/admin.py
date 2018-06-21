from django.contrib import admin

# Register your models here.
from userprofile.models import UserProfileData

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','avatar')
admin.site.register(UserProfileData, ProfileAdmin)