from django.db import models


class Command(models.Model):
    CMDS = (
        ("sm", "Start Motor"),
    )

    cmd = models.CharField(choices=CMDS, max_length=2, default="sm")
    ran = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
