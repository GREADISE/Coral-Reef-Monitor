from django.db import models
from django.contrib.auth.models import User

class coralReef(models.Model):
    name = models.CharField(max_length=1000)
    latitudeC = models.DecimalField(max_digits=9, decimal_places=6)
    longitudeC = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    observer_id = models.PositiveIntegerField()
