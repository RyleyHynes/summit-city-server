from django.db import models

# Step 1: Name the model and inherit the django Model class


class MyHike(models.Model):
    # Step 2: Add any fields on the erd
    summit_user = models.ForeignKey(
        "SummitUser", on_delete=models.CASCADE, related_name="list_hikes")
    hikes = models.ManyToManyField("Hike", related_name="hikes")
