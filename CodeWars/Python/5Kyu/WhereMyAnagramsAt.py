# Link: https://www.codewars.com/kata/where-my-anagrams-at/train/python

# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false

# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. 
# You should return an array of all the anagrams or an empty array if there are none. For example:

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    anagramsList = []
    anagramLetters = {}

    for letter in word:
        if letter in anagramLetters.keys():
            anagramLetters[letter] += 1
        else:
            anagramLetters[letter] = 1

    for wordString in words:
        anagramLettersClone = dict(anagramLetters)
        
        notAnAnagram = False
        if len(wordString) == len(word):
            for character in wordString:

                if character not in anagramLettersClone.keys():
                    notAnAnagram = True
                else:
                    anagramLettersClone[character] -= 1

            if notAnAnagram == False and all(value == 0 for value in anagramLettersClone.values()):
                anagramsList.append(wordString)

        print(anagramLettersClone)

    return anagramsList

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])