from django.db import models

class Attraction(models.Model):
    attraction_type = models.CharField(null=True, max_length=100)