# Link: https://www.codewars.com/kata/sort-out-the-men-from-boys-1/train/java

def men_from_boys(arr):
    even = []
    odd = []
    
    for number in arr:
        if number % 2 == 0:
            if number not in even:
                even.append(number)
        else:
            if number not in odd:
                odd.append(number)
    
    even.sort()
    odd.sort(reverse=True)
    
    return even + odd