def add_letters(*letters):

    if len(letters) == 1:
        return letters[0]
    elif len(letters) == 0:
        return "z"
    else:
        sum = 0

        for letter in letters:
            value = ord(letter) - 96
            sum += value

            if sum > 26:
                sum -= 26

        return chr(sum+96) 


print(add_letters("z","a"))