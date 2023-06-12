import json
import re
from weapons import MeeleWeapon, RangedWeapon


name_pattern = r"^(.*?)\sKEYWORDS"
keyword_pattern = r"KEYWORDS:(.*?)RANGED WEAPONS"  # fix two models
ranged_weapon_pattern = (
    r"RANGED WEAPONS RANGE A BS S AP D (.*?)MELEE WEAPONS RANGE A WS S AP D"
)
melee_weapon_pattern = (
    r"MELEE WEAPONS RANGE A WS S AP D (.*?) FACTION KEYWORDS:"  # fix güllemann
)
characteristic_pattern = (
    r"M T SV W LD OC (\S+ \S+ \S+ \S+ \S+ \S+)"  # fix two characteristics
)
invuln_pattern = r"INVULNERABLE SAVE (.*?)M"
# abilities
core_ability_pattern = r"ABILITIES CORE: (.*?)\s*[A-Z]{3,}"
faction_ability_pattern = r"\nFACTION:\s(.*?)\n"
unit_ability_pattern = r"ABILITIES\n[CORE:.*?]?[FACTION:.*?]?\n(.*?)\n[WARGEAR ABILITIES.*?]?\n[INVULNERABLE SAVE]?"
wargear_ability_pattern = r""
faction_pattern = r"FACTION KEYWORDS:  (.*?)ABILITIES"


def get_substring(regex, string) -> str:
    match = re.search(regex, string)
    if match:
        return match.group(1)
    return ""


def parse_ranged_weapon(weapons_raw: str):
    weapons = re.split(r"(?<=(\s|\d)\d)\s(?=[a-zA-Z])", weapons_raw)
    weapons = [w for w in weapons if w.rstrip()]
    parsed_weapons = []
    for w in weapons:
        w = w.rstrip()
        weapon = create_ranged_weapon(w)
        parsed_weapons.append(weapon)
    return parsed_weapons


def parse_melee_weapon(weapons_raw: str):
    weapons = re.split(r"(?<=(\s|\d)\d)\s(?=[a-zA-Z])", weapons_raw)
    weapons = [w for w in weapons if w.rstrip()]
    parsed_weapons = []
    for w in weapons:
        w = w.rstrip()
        weapon = create_melee_weapon(w)
        parsed_weapons.append(weapon)
    return parsed_weapons


def create_ranged_weapon(w: str):
    weapon = list(filter(None, re.split(r"(?<=.)\s?(?=\d{1,2}\")", w, maxsplit=1)))
    name = weapon[0]
    type = ""
    stats = weapon[1].split(" ")
    ranged_weapon = RangedWeapon(
        name=name,
        type=type,
        range=stats[0],
        attacks=stats[1],
        ballistic_skill=stats[2],
        strength=stats[3],
        armor_penetration=stats[4],
        damage=stats[5],
    )
    return ranged_weapon


def create_melee_weapon(w: str):
    weapon = re.split(r"(?<=.)\s?Melee\s(?=\d)", w)
    name = weapon[0]
    type = ""
    stats = weapon[1].split(" ")
    melee_weapon = MeeleWeapon(
        name=name,
        type=type,
        range="Melee",
        attacks=stats[0],
        weapon_skill=stats[1],
        strength=stats[2],
        armor_penetration=stats[3],
        damage=stats[4],
    )
    return melee_weapon


def create_json(data_list, output_name):
    with open(f"output/{output_name}.json", "w") as file:
        json.dump(
            [ob.__dict__ for ob in data_list],
            file,
            default=lambda o: o.__dict__,
            indent=2,
        )
