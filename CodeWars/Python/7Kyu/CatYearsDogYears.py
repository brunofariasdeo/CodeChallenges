# Link: https://www.codewars.com/kata/cat-years-dog-years-2/python

def owned_cat_and_dog(cat_years, dog_years):
    if cat_years >= 0 and cat_years <15:
        ownedCat = 0
    elif cat_years >= 15 and cat_years < 24:
        ownedCat = 1
    else:
        ownedCat = ((cat_years-24)/4)+2

    if dog_years >= 0 and dog_years <15:
        ownedDog = 0
    elif dog_years >= 15 and dog_years < 24:
        ownedDog = 1
    else:
        ownedDog = ((dog_years-24)/5)+2

    return [int(ownedCat), int(ownedDog)]


