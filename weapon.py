class Weapon:
    def __init__(self, tier, damage):
        self.tier = tier
        self.damage = damage

    def __str__(self):
        return f"{self.tier} weapon"