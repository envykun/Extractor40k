from typing import List

from .characteristic import Characteristic
from weapons import RangedWeapon, MeeleWeapon
from abilities import CoreAbility, FactionAbility, UnitAbility


class Unit:
    def __init__(
        self,
        name: str,
        characteristic: Characteristic,
        ranged_weapons: List[RangedWeapon],
        melee_weapons: List[MeeleWeapon],
        core_abilities: List[CoreAbility],
        faction_abilities: List[FactionAbility],
        unit_abilities: List[UnitAbility],
        keywords: List[str],
        faction: str,
        invuln: str,
    ):
        self.name = name
        self.characteristic = characteristic
        self.ranged_weapons = ranged_weapons
        self.melee_weapons = melee_weapons
        self.core_abilities = core_abilities
        self.faction_abilities = faction_abilities
        self.unit_abilities = unit_abilities
        self.keywords = keywords
        self.faction = faction
        self.invuln = invuln

    def __str__(self):
        return f"Name: {self.name}\n{str(self.characteristic)}\n{str(self.ranged_weapons)}\n{str(self.melee_weapons)}\n{str(self.keywords)}"
