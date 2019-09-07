# Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem

def hourglass(array):
    arrHourglasses = []

    for externIndex, row in enumerate(array):
        if (externIndex + 2) <= len(array) - 1:
            for internIndex,number in enumerate(row):
                arrHourglass = []
                if (internIndex + 2) <= len(row) - 1:
                    arrHourglass.append(sum(row[internIndex:internIndex+3]))
                    arrHourglass.append(array[externIndex+1][internIndex+1])
                    arrHourglass.append(sum(array[externIndex+2][internIndex:internIndex+3]))

                    arrHourglasses.append(sum(arrHourglass))

    return max(arrHourglasses)

# array = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
array = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]] 
print(hourglass(array))
