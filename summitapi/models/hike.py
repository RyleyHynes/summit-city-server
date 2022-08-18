from django.db import models

class Hike(models.Model):
    name= models.CharField(max_length=250)
    distance= models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=200)
    estimated_length = models.TimeField()
    description = models.CharField(max_length=500)
    attractions = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    bucket_list = models.BooleanField(default=False)
    hike_image_url = models.URLField()
    activity = models.ForeignKey("Acitivity", on_delete=models.CASCADE, related_name="hikes" )
    hike_skill_level= models.ForeignKey("HikeSkillLevel", on_delete=models.CASCADE, related_name="hikes")
    
