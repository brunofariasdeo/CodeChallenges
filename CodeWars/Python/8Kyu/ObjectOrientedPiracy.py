# URL: https://www.codewars.com/kata/object-oriented-piracy/train/python

class Ship:
  def __init__(self, draft, crew):
    self.draft = draft
    self.crew = crew
  def is_worth_it(self):
    if (self.draft - self.crew*1.5) > 20:
      return True
    else:
      return False

Titanic = Ship(15, 10)
print(Titanic.is_worth_it())
