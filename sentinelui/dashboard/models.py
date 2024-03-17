from django.db import models
from django.conf import settings


# class mOdel(models.Model):
#     name = models.


class Camera(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    feed_links = models.URLField()
    desc = models.TextField()


class trusted_user(models.Model):
    user =  models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)


# Create your models here.

