from django.db import models

# Champions Model
# Defines the Champions table
class Player(models.Model):
    name = models.CharField("summoner name", max_length=32)
    server = models.CharField("server", max_length=8)
    
    def __unicode__(self):
        return self.name + " [" + self.server + "]"
