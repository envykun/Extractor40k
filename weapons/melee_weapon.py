class MeeleWeapon:
    def __init__(
        self,
        name: str,
        range: str,
        type: str,
        attacks: int,
        weapon_skill: str,
        strength: int,
        armor_penetration: int,
        damage: int,
    ):
        self.name = name
        self.range = range
        self.type = type
        self.attacks = attacks
        self.weapon_skill = weapon_skill
        self.strength = strength
        self.armor_penetration = armor_penetration
        self.damage = damage

    def __str__(self) -> str:
        return f"name: {self.name}, type: {self.type}, Range: {self.range}, A: {self.attacks}, WS: {self.weapon_skill}, S: {self.strength}, AP: {self.armor_penetration}, D: {self.damage}"
