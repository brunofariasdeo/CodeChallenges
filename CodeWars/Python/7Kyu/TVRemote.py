# URL = https://www.codewars.com/kata/tv-remote/python

def tv_remote(word):
    remoteControlKeyboard= ["abcde123","fghij456","klmno789","pqrst.@0","uvwxyz_/"]

    current = [0,0]
    stepsRequired = []

    for letter in word:
        for index, line in enumerate(remoteControlKeyboard):
            if letter in line:
                stepsRequired.append(abs(current[0] - line.index(letter)) + abs(current[1] - index) + 1)
                current[0] = line.index(letter)
                current[1] = index
 
    return sum(stepsRequired)

print(tv_remote("your"))