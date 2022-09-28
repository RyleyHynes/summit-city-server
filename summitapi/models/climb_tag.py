from django.db import models

class ClimbTag(models.Model):
    climb = models.ForeignKey("Climb", on_delete=models.CASCADE, related_name="climb_tags")
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, related_name="climb_tags")