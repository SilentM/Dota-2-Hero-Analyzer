import requests
import json


def runScriptFn():
    r = requests.get("https://api.opendota.com/api/players/107828036/matches")

    with open('sample/output.json', 'w') as out:
        json.dump(r.json(), out, sort_keys=True, indent='\t')

    jsonFile = r.json()

    mapOfHeroKills = {}

    for match in jsonFile:
        hero_id = match["hero_id"]
        hero_kill = match["kills"]
        arrayHeroKill = []
        nameOfHero = ""

        if hero_id in mapOfHeroKills:
            mapOfHeroKills[hero_id] += hero_kill
        else:
            mapOfHeroKills[hero_id] = hero_kill

    with open('heroNameID.json', 'r') as f:
        heroNameID = json.load(f)

    listOfHero = list(heroNameID.values())

    for idValue, kill in mapOfHeroKills.items():
        for heroList in listOfHero:
            for hero in heroList:
                if hero["id"] == idValue:
                    nameOfHero = hero["localized_name"]

                    x = {
                        "id": idValue,
                        "kills": kill,
                        "name": nameOfHero
                    }

                    arrayHeroKill.append(x)

    with open('heroKills.json', 'w') as json_file:
        json.dump(arrayHeroKill, json_file)


runScriptFn()

# constants = requests.get("https://api.opendota.com/api/constants/heroes")
# with open('constants.json', 'w') as out:
#     json.dump(constants.json(), out, sort_keys=True, indent='\t')
#
