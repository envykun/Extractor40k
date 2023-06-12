class Characteristic:
    def __init__(
        self,
        move: str,
        toughness: int,
        save: str,
        wounds: int,
        leadership: str,
        oc: int,
    ):
        self.move = move
        self.toughness = toughness
        self.save = save
        self.wounds = wounds
        self.leadership = leadership
        self.oc = oc

    def __str__(self) -> str:
        return f"M: {str(self.move)}, T: {str(self.toughness)}, Sv: {str(self.save)}, W: {str(self.wounds)}, LD: {str(self.leadership)}, OC: {str(self.oc)}"
