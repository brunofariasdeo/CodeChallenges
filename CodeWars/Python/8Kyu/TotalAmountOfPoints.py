Link: https://www.codewars.com/kata/total-amount-of-points/train/python

def points(games):
    points = 0

    for score in games:
        if score[0] > score[-1]:
            points += 3
        elif score[0] == score[-1]:
            points += 1
        else:
            pass
	
    return points

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))