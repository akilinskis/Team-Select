from django.db import models
from champions.models import Champion

# Composition Model
# Defines the Composition table
class Composition(models.Model):
    name = models.CharField("composition name", max_length=32)

    def __unicode__(self):
        return self.name

# ChampionRole Model
# Defines the ChampionRole table
class ChampionRole(models.Model):
    composition = models.ForeignKey(Composition)
    champion = models.ForeignKey(Champion)
    description = models.TextField("description of champion's role in composition")

    def __unicode__(self):
        return self.champion.name + " in " + self.composition.name

# CompositionCounterList Model
# Defines the CompositionCounterList table
class CompositionCounterList(models.Model):
    composition = models.OneToOneField(Composition)

    def __unicode__(self):
        return self.composition.name + " Counters"

# CompositionCounter Model
# Defines the CompositionCounter table
class CompositionCounter(models.Model):
    composition = models.ForeignKey(Composition)
    compositionlist = models.ForeignKey(CompositionCounterList, verbose_name="list of counters")

    def __unicode__(self):
        return self.compositionlist.composition.name + " vs. " + self.composition.name
