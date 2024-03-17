from django.db import models
from dashboard.models import Camera


class Alerts(models.Model):
    """Alert model for storing alert data."""
    cam_id = models.ForeignKey(Camera, on_delete = models.CASCADE)  # The
    timestamp = models.DateTimeField(auto_now=True)                       # camera
    activity = models.CharField(max_length=100)
    img = models.ImageField(upload_to='alert_snapshots/', default='profile.svg')

    

# Create your models here.
