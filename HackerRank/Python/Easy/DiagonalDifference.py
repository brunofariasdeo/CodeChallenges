def diagonalDifference(arr):
    leftToRight = []
    rightToLeft = []

    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if i == j:
                leftToRight.append(arr[i][j])
            
    for i in range(0,len(arr)):
        for j in range(len(arr)-1,-1,-1):
            rightToLeft.append(arr[i][j])
            i+=1
            j-=1

        if len(rightToLeft) == len(arr):
            break

    return abs(sum(leftToRight) - sum(rightToLeft))

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))