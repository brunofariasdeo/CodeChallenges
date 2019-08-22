# Link: https://www.codewars.com/kata/remove-duplicate-words/train/python

def remove_duplicate_words(s):
    s = s.split()

    finalList = [] 
    for word in s: 
        if word not in finalList: 
            finalList.append(word)

    return ' '.join(finalList) 

print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))