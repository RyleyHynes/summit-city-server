from django.db import models

# Step 1: Name the model and inherit the django Model class


class ListHike(models.Model):
    # Step 2: Add any fields on the erd
    hike = models.ForeignKey(
        "Hike", on_delete=models.CASCADE, related_name="list_hikes")
    my_hike = models.ForeignKey(
        "MyHike", on_delete=models.CASCADE, related_name="list_hikes")
