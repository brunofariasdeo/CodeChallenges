def abbrevName(name):
    name = name.split()
    abbrevString = ""

    for letter in name:
        abbrevString += letter[0] + "."
    
    return abbrevString[:-1]

print(abbrevName("Sam Harris"))