class Warrior():

    def __init__(self, level=1, experience = 100, rank = "Pushover", achievements = []):
        self.level = level
        self.experience = experience
        self.rank = rank
        self.achievements = []

    def setLevel(self):
        if (self.experience // 100) != self.level:
            print("The warrior has leveled up! Congratulations for all the hard work.")
            print(self.experience//100)
            self.level = self.experience // 100

    def setExperience (self, experience):
        if ((self.experience + experience)<=10000):
            self.experience += experience
        else:
            self.experience = 10000

    def setRank(self):
        tiers = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

        if (tiers[self.level//10]) != self.rank:
            print("The warrior has reached a new rank! Congratulations for all the hard work.")
            self.rank = tiers[self.level//10]

    def getRank(self, level):
        tiers = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

        rank = level//10
        return rank + 1

    def battle(self, enemyLevel):
        tiers = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

        if (enemyLevel not in range(1,101)):
            return "Invalid level"
        else:
            print("Early Self:" , self.level)
            print("Early Enemy:", enemyLevel)

            if (self.level == enemyLevel):
                self.setExperience(10)
            elif ((self.level - enemyLevel) == 1):
                self.setExperience(5)
            elif ((self.level - enemyLevel) == 2):
                self.setExperience(0)
            elif ((self.level - enemyLevel) < 0):
                selfRank = [self.getRank(self.level),self.rank]
                print("Self", selfRank)
                enemyRank = [self.getRank(enemyLevel),tiers [enemyLevel//10]]
                print("Enemy", enemyRank)
                if ((enemyRank[0] - selfRank[0])< 1 or ((enemyLevel - self.level) < 5)):
                    self.setExperience(20 * ((enemyLevel - self.level)**2))
                else:
                    print("You've been defeated")
                    return "You've been defeated"
        
        
        print("Final Self:" , self.level)
        print("Final Enemy:", enemyLevel)
        
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
            print("Value is not a list. You will not be able to join the training.")
        else:
            if len(value) != 3:
                print("Your list can only have 3 elements. You will not be able to join the training.")
            else:
                if value[2] <= self.level:
                    print("dale")
                    self.setExperience(value[1])
                    self.achievements.append(value[0])
                    self.setLevel()
                    self.setRank()
                    return value[0]
                else:
                    print("You are not allowed to take this training.")
                    return "Not strong enough"
