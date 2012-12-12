from django.db import models

# Champions Model
# Defines the Champions table
class Champion( models.Model ):
    name = models.CharField( "champion name", max_length=32)
    
    def __unicode__(self):
        return self.name
