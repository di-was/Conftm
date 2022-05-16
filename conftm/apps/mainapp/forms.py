from django.forms import ModelForm
from conftm.apps.mainapp.models import *
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ConfessionsForm(ModelForm):
    class Meta:
        model = Confessions
        fields = ['content', 'parent']


class Appform(ModelForm):
    class Meta:
        model = Apps
        fields = ['name', 'AccessToken', 'pageId', 'parent']


