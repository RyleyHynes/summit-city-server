from django.db import models


class Climb(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=250)
    climb_image_url = models.URLField()
    activity = models.ForeignKey(
        "Activity", on_delete=models.CASCADE, related_name="climbs")
    climb_type = models.ForeignKey(
        "ClimbType", on_delete=models.CASCADE, related_name="climbs")
    grade = models.ForeignKey(
        "Grade", on_delete=models.CASCADE, related_name="climbs")
    tags = models.ManyToManyField("Tag", through="ClimbTag", related_name="climbs")
