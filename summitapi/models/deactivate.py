from django.db import models


class Deactivate(models.Model):

    deactivatedUser = models.ForeignKey("SummitUser", on_delete=models.CASCADE, related_name="deactivate")
    approveUser = models.ForeignKey("SummitUser", on_delete=models.CASCADE, related_name="firstdeactiveapproved")
    secondApproveUser = models.ForeignKey("SummitUser", on_delete=models.CASCADE, related_name="seconddeactiveapproved", null=True)