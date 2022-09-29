from django.db import models


class Demote(models.Model):

    demotedUser = models.ForeignKey("SummitUser", on_delete=models.CASCADE, related_name="demoted")
    approveUser = models.ForeignKey("SummitUser", on_delete=models.CASCADE, related_name="firstapproved")
    secondApproveUser = models.ForeignKey("SummitUser", on_delete=models.CASCADE, related_name="secondapproved", null=True)