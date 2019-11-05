class Warrior():

    def __init__(self, level=1, experience = 100, rank = "Pushover", achievements = []):
        self.level = level
        self.experience = experience
        self.rank = rank
        self.tiers = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.achievements = []

    def setLevel(self):
        if (self.experience // 100) != self.level:
            self.level = self.experience // 100

    def setExperience (self, experience):
        if ((self.experience + experience)<=10000):
            self.experience += experience
        else:
            self.experience = 10000

    def setRank(self):
        if (self.tiers[self.level//10]) != self.rank:
            self.rank = self.tiers[self.level//10]

    def getRank(self, level):
        rank = level//10
        return rank + 1

    def battle(self, enemyLevel):
        if (enemyLevel not in range(1,101)):
            return "Invalid level"
        else:
            if (self.level == enemyLevel):
                self.setExperience(10)
            elif ((self.level - enemyLevel) == 1):
                self.setExperience(5)
            elif ((self.level - enemyLevel) == 2):
                self.setExperience(0)
            elif ((self.level - enemyLevel) < 0):
                selfRank = [self.getRank(self.level),self.rank]
                enemyRank = [self.getRank(enemyLevel),self.tiers [enemyLevel//10]]

                if ((enemyRank[0] - selfRank[0])< 1 or ((enemyLevel - self.level) < 5)):
                    self.setExperience(20 * ((enemyLevel - self.level)**2))
                else:
                    return "You've been defeated"
        
        if ((self.level - enemyLevel) >= 2):
            self.setLevel()
            self.setRank()
            return "Easy fight"
        elif ((self.level - enemyLevel) >= 0 and (self.level - enemyLevel) < 2) :
            self.setLevel()
            self.setRank()
            return "A good fight"
        elif ((self.level - enemyLevel) <= 0):
            self.setLevel()
            self.setRank()
            return "An intense fight"

    def training(self, value):
        if not isinstance(value, list):
            return "Value is not a list. You will not be able to join the training."
        else:
            if len(value) != 3:
                return "Your list can only have 3 elements. You will not be able to join the training."
            else:
                if value[2] <= self.level:
                    self.setExperience(value[1])
                    self.achievements.append(value[0])
                    self.setLevel()
                    self.setRank()
                    return value[0]
                else:
                    return "Not strong enough"
