# URL: https://www.codewars.com/kata/color-ghost/train/python

import random

class Ghost(object):
  colors = ["white","yellow","purple","red"]
  def __init__(self):
      self.color = self.colors[random.randint(1,3)]

ghost = Ghost()
print(ghost.color)