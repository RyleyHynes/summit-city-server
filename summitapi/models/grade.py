from django.db import models

class Grade(models.Model):
    rating = models.DecimalField()