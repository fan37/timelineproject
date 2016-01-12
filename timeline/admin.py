from django.contrib import admin

from timeline.models import *

# Register your models here.

admin.site.register(Message)
admin.site.register(Like)
admin.site.register(UserProfile)

