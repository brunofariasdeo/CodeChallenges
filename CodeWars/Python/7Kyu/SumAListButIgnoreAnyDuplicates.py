# URL: https://www.codewars.com/kata/sum-a-list-but-ignore-any-duplicates/train/python

def sum_no_duplicates(l):
    dictionary = {}
    sum = 0
    
    for i in l:
    	if i in dictionary.keys():
		    dictionary[i]+=1
    	else:
    		dictionary[i]=1

    for i in dictionary:
    	if dictionary[i] == 1:
    		sum += i
            
    return sum

print(sum_no_duplicates([1, 1, 2, 3]))