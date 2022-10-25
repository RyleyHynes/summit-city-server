from django.db import models

# Step 1: Name the model and inherit the django Model class


class MyClimb(models.Model):
    # Step 2: Add any fields on the erd
    completed = models.BooleanField(default=False)
    bucket_list = models.BooleanField(default=False)
    summit_user = models.ForeignKey(
        "SummitUser", on_delete=models.CASCADE, related_name="list_climbs")
    climbs = models.ManyToManyField("Climb", related_name="climbs")
