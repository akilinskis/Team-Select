from django.db import models
# from counters.models import CounterList
# from attributes.models import Attribute
# from compositions.models import Composition

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
    # Will uncomment these once implemented
    # counters = models.OneToOneField(CounterList, verbose_name="champion counters", primary_key=True)
    # attributes = models.ManyToManyField(Attribute)
    # compositions = models.ManyToManyField(Composition)
    

    def __unicode__(self):
        return self.name
