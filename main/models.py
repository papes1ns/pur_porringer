from django.db import models


class Log(models.Model):
    ran = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.ran
