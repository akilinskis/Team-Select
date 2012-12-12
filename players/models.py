from django.db import models

# Champions Model
# Defines the Champions table
class Player( models.Model ):
    name = models.CharField( "summoner name", max_length=32)
    
    def __unicode__(self):
        return self.name
