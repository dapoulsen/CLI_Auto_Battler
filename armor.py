class Armor:
    _tiers = ["None", "Makeshift", "Bronze", "Silver", "Gold", "Diamond"]

    def __init__(self):
        self.tier = 0
        self.value = 0
    
    def upgrade_armor(self):
        if self.tier == len(self._tiers)-1:
            print("You have the best armor there is!")
            return
        self.tier += 1
        self.value = self.tier * 5
        print(f"You have upgraded your {self._tiers[self.tier-1]} armor to a {self.show_tier()} armor")

    def reset_armor(self):
        self.value = self.tier * 5

    def show_tier(self):
        return self._tiers[self.tier]