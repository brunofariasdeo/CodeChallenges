# Link: https://www.codewars.com/kata/how-good-are-you-really/train/python

def better_than_average(class_points, your_points):
    average = sum(class_points)/len(class_points)
    
    if your_points>average:
        return True
    else:
        return False