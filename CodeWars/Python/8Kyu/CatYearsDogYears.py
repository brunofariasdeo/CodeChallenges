# Link: https://www.codewars.com/kata/cat-years-dog-years/train/python

def human_years_cat_years_dog_years(human_years):

    if human_years == 1:
        catYears = 15 
        dogYears = 15 
    elif human_years == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + human_years*4
        dogYears = 15 + 9 + human_years*5

    return [human_years,catYears,dogYears]