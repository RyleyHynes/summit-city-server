from django.db import models


class Activity(models.Model):
    type = models.CharField(max_length=55)
    activity_image_url = models.URLField()