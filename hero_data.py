class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
class Tank(Hero):
    def __init__(self, name):
        super().__init__(name, "Tank")


class Support(Hero):
    def __init__(self, name):
        super().__init__(name, "Support")


class DPS(Hero):
    def __init__(self, name):
        super().__init__(name, "Damage")

HEROES = {
    "D.Mon": Tank("D.Mon"),
    "D.va": Tank("D.va"),
    "Domina": Tank("Domina"),
    "Doomfist": Tank("Doomfist"),
    "Hazard": Tank("Hazard"),
    "Junker Queen": Tank("Junker Queen"),
    "Mauga": Tank("Mauga"),
    "Orisa": Tank("Orisa"),
    "Ramattra": Tank("Ramattra"),
    "Reinhardt": Tank("Reinhardt"),
    "Roadhog": Tank("Roadhog"),
    "Sigma": Tank("Sigma"),
    "Winston": Tank("Winston"),
    "Wrecking Ball": Tank("Wrecking Ball"),
    "Zarya": Tank("Zarya"),
    "Anran": DPS("Anran"),
    "Ashe": DPS("Ashe"),
    "Bastion": DPS("Bastion"),
    "Cassidy": DPS("Cassidy"),
    "Echo": DPS("Echo"),
    "Emre": DPS("Emre"),
    "Freja": DPS("Freja"),
    "Genji": DPS("Genji"),
    "Hanzo": DPS("Hanzo"),
    "Junkrat": DPS("Junkrat"),
    "Mei": DPS("Mei"),
    "Pharah": DPS("Pharah"),
    "Reaper": DPS("Reaper"),
    "Shion": DPS("Shion"),
    "Sierra": DPS("Sierra"),
    "Sojourn": DPS("Sojourn"),
    "Soldier: 76": DPS("Soldier: 76"),
    "Symmetra": DPS("Symmetra"),
    "Torbjörn": DPS("Torbjörn"),
    "Tracer": DPS("Tracer"),
    "Vendetta": DPS("Vendetta"),
    "Venture": DPS("Venture"),
    "Widowmaker": DPS("Widowmaker"),
    "Ana": Support("Ana"),
    "Baptiste": Support("Baptiste"),
    "Brigitte": Support("Brigitte"),
    "Doctrine": Support("Doctrine"),
    "Illari": Support("Illari"),
    "Jetpack Cat": Support("Jetpack Cat"),
    "Juno": Support("Juno"),
    "Kiriko": Support("Kiriko"),
    "Lifeweaver": Support("Lifeweaver"),
    "Lúcio": Support("Lúcio"),
    "Mercy": Support("Mercy"),
    "Mizuki": Support("Mizuki"),
    "Moira": Support("Moira"),
    "Sombra": Support("Sombra"),
    "Wuyang": Support("Wuyang"),
    "Zenyatta": Support("Zenyatta"),
}