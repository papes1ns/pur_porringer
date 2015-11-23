from django.db import models


class Log(models.Model):
    ran = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.ran
