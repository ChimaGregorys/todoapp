from django.db import models

# Create your models here.
class Task(models.Model):
    """Our Task Model"""
    created_at = models.DateTimeField(auto_now_add=True)
    name       = models.CharField(max_length=256)
    completed  = models.BooleanField(default=False)
