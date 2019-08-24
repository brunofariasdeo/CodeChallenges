# Link: https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    arr = arr.split()
    arr = list(map(int, arr))
    sumValues = []

    for index, item in enumerate(arr):
        tempArr = list(arr)
        del tempArr[index]
        sumValues.append(sum(tempArr))

    return str(min(sumValues)) + " " + str(max(sumValues))

print(miniMaxSum("1 2 3 4 5"))