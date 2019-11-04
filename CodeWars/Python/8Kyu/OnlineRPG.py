# URL: https://www.codewars.com/kata/online-rpg-player-to-qualifying-stage/train/python

def playerRankUp(pts):
    if pts >= 100:
        return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
    else:
        return False
    
print(playerRankUp(101))