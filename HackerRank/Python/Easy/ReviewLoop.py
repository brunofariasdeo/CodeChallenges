def oddEvenSeparated(word):
    odd = ""
    even = ""

    for index, letter in enumerate(word):
        if index % 2 == 0 :
            odd += letter
        else:
            even += letter

    return print(odd + " " + even)

T = int(input())

for number in range (0,T):
    word = input()
    oddEvenSeparated(word)
