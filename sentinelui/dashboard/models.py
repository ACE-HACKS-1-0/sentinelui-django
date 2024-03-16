from django.db import models

# class mOdel(models.Model):
#     name = models.


class Camera(models.Model):
    name = models.CharField(max_length=20)
    feed_links = models.URLField()
    desc = models.TextField()

# Create your models here.

