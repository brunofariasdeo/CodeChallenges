# Link: https://www.codewars.com/kata/see-you-next-happy-year/train/python

from collections import Counter

def next_happy_year(year):
    happyYear = False

    while (happyYear == False):
        if all(x == 1 for x in Counter(str(year)).values()):
            return year
        else:
            year += 1

print(next_happy_year(1001))