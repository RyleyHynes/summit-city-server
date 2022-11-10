from django.db import models

# Step 1: Name the model and inherit the django Model class


class ListClimb(models.Model):
    # Step 2: Add any fields on the erd
    climb = models.ForeignKey(
        "Climb", on_delete=models.CASCADE, related_name="list_climbs")
    my_climb = models.ForeignKey(
        "MyClimb", on_delete=models.CASCADE, related_name="list_climbs")
