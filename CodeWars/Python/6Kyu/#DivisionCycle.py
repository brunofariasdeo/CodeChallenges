# Link: https://www.codewars.com/kata/count-odd-numbers-below-n/discuss#5d58142c04ffd00012b5b603
from collections import Counter

def Cycle(number):
    division = str(1/number)
    cnt = Counter()

    for number in division[2:]:
        cnt[number]+=1

    return int(len(division[2:])/(max(cnt.values())))

print(Cycle(11))
print(Cycle(22))
print(Cycle(27))