# Link: https://www.codewars.com/kata/the-lamp-revisited/train/python

class Lamp():
    def __init__(self,color,on=False):
        self.color = color
        self.on = on
    def toggle_switch(self):
        if self.on:
            self.on = False
        else:
            self.on = True
    def state(self):
        if self.on:
            return "The lamp is on."
        else:
            return "The lamp is off."

