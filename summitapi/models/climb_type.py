from django.db import models

class ClimbType(models.Model):
    name = models.CharField(max_length=100)
    