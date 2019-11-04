class Warrior():
    def __init__(self, level=10, experience = 100, rank = "Pushover", achievements = []):
        self.level = level
        self.experience = experience
        self.rank = rank
        self.achievements = achievements

    def levelUp(self.experience):
        pass

    def battle():
        pass

    def training(self, value):
        if not isinstance(value, list):
            print("Value is not a list. You will not be able to join the training.")
        else:
            if len(value) != 3:
                print("Your list can only have 3 elements. You will not be able to join the training.")
            else:
                if value[2] <= self.level:
                    self.experience += value[1]
                    print(value[0])


tom = Warrior()
print(tom.level)
print(tom.experience)
print(tom.rank)
print(tom.training(["Defeated Chuck Norris",100,1]))
print(tom.experience)

# bruce_lee = Warrior()
# print(tom.level)
# print(tom.experience)
# print(tom.rank)