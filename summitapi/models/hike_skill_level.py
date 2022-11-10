from django.db import models


class HikeSkillLevel(models.Model):
    level = models.CharField(max_length=100)
