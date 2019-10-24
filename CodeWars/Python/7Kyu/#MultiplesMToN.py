# Link: https://www.codewars.com/kata/return-the-first-m-multiples-of-n/train/python

def multiples(m, n):
    multiplesList = []
    
    for number in range(n, (m*n)+1, n):
        multiplesList.append (number)
        
    return multiplesList