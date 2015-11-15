from django.db import models


class ip(models.Model):
    ip = models.CharField(max_length=16)
    active = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.ip
