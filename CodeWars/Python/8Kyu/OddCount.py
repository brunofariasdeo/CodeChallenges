# Link: https://www.codewars.com/kata/count-odd-numbers-below-n/python

# Given a number n, return the number of positive odd numbers below n, EASY!

# oddCount(7) //=> 3, i.e [1, 3, 5]
# oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
# Expect large Inputs!

def odd_count(n):
    count = 0

    for number in range (1,n):
        if number%2 != 0:
            count+=1

    return count

print(odd_count(15))

    