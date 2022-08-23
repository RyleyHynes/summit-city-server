from django.db import models

class Grade(models.Model):
    rating = models.DecimalField(decimal_places=3, max_digits=4)
    