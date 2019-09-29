class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        alpha = (sum(self.scores))/2

        if alpha >= 90 and alpha <= 100:
            return "O"
        elif alpha >= 80 and alpha <= 90:
            return "E"
        elif alpha >= 70 and alpha <= 80:
            return "A"
        elif alpha >= 55 and alpha <= 70:
            return "P"
        elif alpha >= 40 and alpha <= 55:
            return "D"
        elif alpha <40:
            return "T"

# line = input().split()
# firstName = line[0]
firstName = "Heraldo"
# lastName = line[1]
lastName = "Memelli"
# idNum = line[2]
idNum = 8135627
# numScores = int(input()) # not needed for Python
# scores = list( map(int, input().split()) )
scores = [100, 80]
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
