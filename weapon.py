class Weapon:
    _tiers = ["Basic", "Wood", "Bronze", "Silver", "Gold", "Diamond"]

    def __init__(self):
        self.tier = 0
        self.damage = 2

    def upgrade_tier(self):
        if self.tier == len(self._tiers):
            print("You have maximum tier weapon!")
            return
        self.tier += 1
        self.damage *= 2
        print(f"You have upgraded your {self._tiers[self.tier-1]} weapon to a {self.show_tier()} weapon")

    def show_tier(self):
        return self._tiers[self.tier]

    def __str__(self):
        return f"{self._tiers[self.tier]} weapon"