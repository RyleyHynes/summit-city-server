from django.db import models


class Hike(models.Model):
    user = models.ForeignKey("SummitUser", on_delete=models.CASCADE, related_name="hikes")
    name = models.CharField(max_length=250)
    distance = models.DecimalField(decimal_places=4, max_digits=10)
    location = models.CharField(max_length=200)
    estimated_length = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    bucket_list = models.BooleanField(default=False)
    hike_image_url = models.URLField()
    activity = models.ForeignKey(
        "Activity", on_delete=models.CASCADE, related_name="hikes")
    hike_skill_level = models.ForeignKey(
        "HikeSkillLevel", on_delete=models.CASCADE, related_name="hikes")
    tags = models.ManyToManyField("Tag", through="HikeTag", related_name="hikes")
