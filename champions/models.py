from django.db import models

# Champions Model
# Defines the Champions table
# Proper weight usage would have the sum of the five weights as 100
class Champion(models.Model):
    name = models.CharField("champion name", max_length=32)
    top = models.IntegerField("top lane position weight")
    jungle = models.IntegerField("jungle position weight")
    mid = models.IntegerField("mid lane position weight")
    adc = models.IntegerField("ad bottom lane position weight")
    support = models.IntegerField("support bottom lane position weight")
    

    def __unicode__(self):
        return self.name
