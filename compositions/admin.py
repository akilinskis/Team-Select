from compositions.models import Composition
from compositions.models import ChampionRole
from compositions.models import CompositionCounterList
from compositions.models import CompositionCounter
from django.contrib import admin

admin.site.register(Composition)
admin.site.register(ChampionRole)
admin.site.register(CompositionCounterList)
admin.site.register(CompositionCounter)
