def tv_remote(word):
    remoteControlKeyboard= [["abcde123"],["fghij456"],["klmno789"],["pqrst.@0"],["uvwxyz_/"]]
    stepsRequired = []

    for letter in word:
        current = letter
        for index,buttons in enumerate(remoteControlKeyboard):

            if current in buttons:
                
            print(index,buttons)

print(tv_remote("dale"))