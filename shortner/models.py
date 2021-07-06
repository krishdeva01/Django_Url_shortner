from django.db import models

class mymodel(models.Model):

    old_url = models.URLField(max_length=1000)
    new_url = models.CharField(max_length=10)
    time_created = models.DateTimeField()

    def __str__(self):
        return self.old_url
