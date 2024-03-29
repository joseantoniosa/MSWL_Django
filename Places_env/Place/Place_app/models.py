from django.db import models

class Place(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    date = models.DateTimeField(auto_now_add=True, auto_now = True)
    nr_views = models.IntegerField()
    url = models.URLField( max_length=200 )

    def __unicode__(self):
        return self.name

