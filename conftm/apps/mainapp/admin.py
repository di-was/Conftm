from django.contrib import admin
from conftm.apps.mainapp.models import UserProfile, Confessions, Apps, Confessed
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Apps)
admin.site.register(Confessions)
admin.site.register(Confessed)