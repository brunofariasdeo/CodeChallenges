# Link = https://www.codewars.com/kata/baby-shark-lyrics-generator/train/python

def baby_shark_lyrics():
  s=[]
  term=["Baby shark","Mommy shark","Daddy shark","Grandma shark","Grandpa shark","Let's go hunt"]
  repeat=["doo doo doo doo doo doo","Run away,…"]

  for words in term:
    s+=3*[words+", "+repeat[0]]
    s+=[words+"!"] 

  return '\n'.join(s)+'\n'+"Run away,…"

print(baby_shark_lyrics())