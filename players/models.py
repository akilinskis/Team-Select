from django.db import models

# Champions Model
# Defines the Champions table
# Proper weight usage would have all fields sum to 100
class Player(models.Model):
    name = models.CharField("summoner name", max_length=32)
    top = models.IntegerField("top lane position weight")
    jungle = models.IntegerField("jungle position weight")
    mid = models.IntegerField("mid lane position weight")
    adc = models.IntegerField("ad carry position weight")
    support = models.IntegerField("support position weight")
    counters = models.ManyToManyField(Champion)
    attributes = models.ManyToManyField(Attribute)
    
    def __unicode__(self):
        return self.name
