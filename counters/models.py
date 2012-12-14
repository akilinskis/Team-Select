from django.db import models
from champions.models import Champion

# CounterList Model
# Defines the CounterList table
class CounterList(models.Model):
    champion = models.OneToOneField(Champion)

    def __unicode__(self):
        return self.champion.name + " Counters"

# Counter Model
# Defines the Counter table
class Counter(models.Model):
    champion = models.ForeignKey(Champion)
    strength = models.IntegerField("counter strength (out of 100)")
    championlist = models.ForeignKey(CounterList, verbose_name="list of counters")

    def __unicode__(self):
        return self.championlist.champion.name + " vs. " + self.champion.name
