import math   

def largestPower(N):

    if N>=1.67 and N<= 3:
        return 0
    elif N>0 and N<1.67:
        return - 1
    else:
        logResult = int((math.log(N,2))/(math.log(3,2)))

        
        return int((math.log(N,2))/(math.log(3,2)))


print(largestPower(80))