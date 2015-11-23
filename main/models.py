from django.db import models


class Log(models.Model):
    ran = models.DateTimeField()

    def __unicode__(self):
        return self.ran
