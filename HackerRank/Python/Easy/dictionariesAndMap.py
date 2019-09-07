N = int(input())
dictionary = {}

for i in range(1,N+1):
    info = input()
    info = info.split()

    dictionary[info[0]] = info[1]

while True:
    try:  
        hackerRankStr = input()
        if hackerRankStr in dictionary.keys():
            print(hackerRankStr + "=" + dictionary[hackerRankStr])
        else:
            print("Not found")
    except EOFError:
        break
    