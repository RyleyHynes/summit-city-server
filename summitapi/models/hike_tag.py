from django.db import models

class HikeTag(models.Model):
    hike = models.ForeignKey("Hike", on_delete=models.CASCADE, related_name="hike_tags")
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, related_name="hike_tags")