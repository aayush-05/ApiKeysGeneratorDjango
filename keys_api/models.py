from datetime import datetime
from django.db import models

# Create your models here.
class RandomKey(models.Model):
    api_key = models.CharField(max_length=40)
    is_blocked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    last_alive_call = models.DateTimeField(default=datetime.now, blank=True)
class AvailableKey(models.Model):
    key = models.OneToOneField(RandomKey, on_delete=models.CASCADE, primary_key=False)
