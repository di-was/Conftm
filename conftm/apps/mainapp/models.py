from django.db import models
from django.contrib.auth.models import User
import json
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)

    def __Str__(self):
        return self.user.username


class Apps(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    parent = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    AccessToken = models.CharField(max_length=10000, blank=False, null=False)
    pageId = models.IntegerField(unique=True)
    url = models.URLField(default="https://conftm.herokuapp.com/")
    def __str__(self):
        return self.name

    def info(self):
        dictionary = {"name": self.name, "url": self.url + str(self.pageId) + '/', "confessions": len(self.confessions_set.all()), "pageId": self.pageId}
        return dictionary


class Confessions(models.Model):
    content = models.CharField(max_length=5000, blank=False, null=False)
    parent = models.ForeignKey(Apps, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.content


class Confessed(models.Model):
    content = models.CharField(max_length=5000, blank=False, null=False)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.content
