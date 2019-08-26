# Link: https://www.codewars.com/kata/powers-of-3/train/python

def largestPower(N):
    largest = 0

    for number in range (0,N):
        if 3**(number) < N:
            largest = number

    return largest

print(largestPower(1000))
    