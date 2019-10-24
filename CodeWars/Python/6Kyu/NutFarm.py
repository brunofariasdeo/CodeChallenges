# Link: https://www.codewars.com/kata/nut-farm/train/python

def shake_tree(tree):

    position = (len(tree[0]))*[0]

    for index, row in enumerate(tree):
        for innerIndex, item in enumerate(row):
            index = 0
            if item == "o":
                nutFound = True
                while nutFound == True:
                    if index+1 < len(tree):
                        index+=1
                        if tree[index][innerIndex] == "/":
                            if innerIndex+1<= len(row):
                                innerIndex-=1
                        elif tree[index][innerIndex] == "\\":
                            if innerIndex+1<= len(row):
                                innerIndex+=1
                        elif tree[index][innerIndex] == "_":
                            break

                    if index == len(tree)-1:
                        nutFound = False
                        position[innerIndex] += 1

    return position

a = [' o o o  ', ' /    / ', '   /    ', '  /  /  ', '   ||   ', '   ||   ', '   ||   ']
print(shake_tree(a))