def compareTriplets(a, b):
    Alice = 0
    Bob = 0

    for i in (range(0,3)):
        if a[i] > b[i]:
            Alice+=1
        elif a[i] == b[i]:
            pass
        else:
            Bob+=1

    return str(Alice) + str(Bob)

print(compareTriplets([5, 6, 7], [3, 6, 10]))