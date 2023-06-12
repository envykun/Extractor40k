class RangedWeapon:
    def __init__(
        self,
        name: str,
        type: str,
        range: str,
        attacks: int,
        ballistic_skill: str,
        strength: int,
        armor_penetration: int,
        damage: int,
    ):
        self.name = name
        self.type = type
        self.range = range
        self.attacks = attacks
        self.ballistic_skill = ballistic_skill
        self.strength = strength
        self.armor_penetration = armor_penetration
        self.damage = damage

    def __str__(self) -> str:
        return f"name: {self.name}, type: {self.type}, Range: {self.range}, A: {self.attacks}, BS: {self.ballistic_skill}, S: {self.strength}, AP: {self.armor_penetration}, D: {self.damage}"
