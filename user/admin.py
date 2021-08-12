from django.contrib import admin
from user.models import Profile
from django.contrib.auth.models import User


admin.site.register(Profile)
# admin.site.unregister(User)


