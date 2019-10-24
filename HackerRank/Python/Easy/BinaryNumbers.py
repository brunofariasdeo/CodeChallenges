# Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem

def binaryNumbers (n):
    consecutiveOnes = []
    binary = bin(n)[2:] 

    previous = ""
    consecutive = 1
    for number in list(binary):
        if number == previous and number == "1":
            consecutive += 1
        else:
            consecutiveOnes.append(consecutive)
            consecutive = 1

        previous = number
    consecutiveOnes.append(consecutive)

    return max(consecutiveOnes)

print(binaryNumbers(439))