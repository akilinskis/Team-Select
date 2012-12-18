# Parsing logic for parsing a JSON file into the database.
# TODO: Add functionality for parsing team compositions.
# TODO: Add security that requires admin credentials

from django.http import HttpResponse
from django.http import Http404
from champions.models import Champion
from counters.models import Counter, CounterList
from compositions.models import Composition, ChampionRole, CompositionCounter, CompositionCounterList
from django.utils import simplejson
from django.core.exceptions import ObjectDoesNotExist

CONFIG_FILE_PATH = "config/config.json"

# flush_all_tables - Clears out all current databases entries
def flush_all_tables():
    Champion.objects.all().delete()
    Counter.objects.all().delete()
    CounterList.objects.all().delete()
    Composition.objects.all().delete()
    ChampionRole.objects.all().delete()
    CompositionCounter.objects.all().delete()
    CompositionCounterList.objects.all().delete()

# update_positions - Fills in position info for a Champion object
def update_positions(champion, positions):
    champion.top = positions["top"]
    champion.jungle = positions["jungle"]
    champion.mid = positions["mid"]
    champion.adc = positions["adc"]
    champion.support = positions["support"]
    champion.save()

# update_counters - Fills in Counter info for a Champion
def update_counters(champion, counters):
    for counter in counters:
        championcounter = None
        try:
            championcounter = Champion.objects.get(name=counter["name"])
        except ObjectDoesNotExist:
            championcounter = Champion(name=counter["name"], top=0, jungle=0, mid=0, adc=0, support=0)
            championcounter.save()
            counterlist = CounterList(champion=championcounter)
            counterlist.save()
        counterlist = champion.counterlist
        c = Counter(champion=championcounter, strength=counter["strength"], championlist=counterlist)
        c.save()

# update_champion_compositions - Adds ChampionRole objects, links everything appropriately
def update_champion_compositions(champion, compositions):
    for composition in compositions:
        compositionobject = None
        try:
            compositionobject = Composition.objects.get(name=composition["name"])
        except ObjectDoesNotExist:
            compositionobject = Composition(name=composition["name"])
            compositionobject.save()
            compcounterlist = CompositionCounterList(composition=compositionobject)
            compcounterlist.save()
        championroleobject = ChampionRole(composition=compositionobject, champion=champion, description=composition["description"])
        championroleobject.save()

# reload_configs - Gets called by URL, flushes and reloads all database entries.
def reload_configs(request):
    flush_all_tables()
    response = {}
    json_data = open(CONFIG_FILE_PATH, "r")
    try:
        configjson = simplejson.load(json_data)
    except ValueError:
        response['status_code'] = 400
        response["response"] = "Error parsing json file"
        return HttpResponse(simplejson.dumps(response), mimetype="application/json")
    json_data.close()
    champions = configjson["champions"]
    for champion in champions:
        championobject = None
        try:
            championobject = Champion.objects.get(name=champion["name"])
        except ObjectDoesNotExist:
            positions = champion["positions"]
            championobject = Champion(name=champion["name"], top=positions["top"], jungle=positions["jungle"], mid=positions["mid"], adc=positions["adc"], support=positions["support"])
            championobject.save()
            counterlist = CounterList(champion=championobject)
            counterlist.save()
        else:
            update_positions(championobject, champion["positions"])
        update_counters(championobject, champion["counters"])
        update_champion_compositions(championobject, champion["compositions"])
    response['status_code'] = 200
    response["response"] = "Reload successful"
    return HttpResponse(simplejson.dumps(response), mimetype="application/json")
