def staircase(n):
    staircaseList = []
    for i in range(1,n+1):
        for j in range(n,-1,-1):
            if (i + j) == n:
                staircaseList.append(j*" " + i*"#" )

    return print('\n'.join(staircaseList))

staircase(6)