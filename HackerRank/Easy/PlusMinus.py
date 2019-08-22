def plusMinus(arr):
    totalZeros = 0
    totalNegatives = 0
    totalPositives = 0

    for number in arr:
        if number < 0:
            totalNegatives += 1
        elif number == 0:
            totalZeros += 1
        else:
            totalPositives+=1
    
    print(totalPositives/len(arr))
    print(totalNegatives/len(arr))
    print(totalZeros/len(arr))