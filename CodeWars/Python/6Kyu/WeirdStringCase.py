# Link: https://www.codewars.com/kata/weird-string-case

def to_weird_case(string):
    weirdList = []
    string = string.split()

    for index1, item1 in enumerate(string):
        subString = list(item1)
        for index, item in enumerate(subString):
            if item.isalpha():
                if index % 2 == 0:
                    subString[index] = item.upper()
                else:
                    subString[index] = item.lower()
        weirdList.append(''.join(subString))
    return ' '.join(weirdList)

print(to_weird_case('string'))