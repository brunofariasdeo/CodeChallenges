def string_to_array(s):
    s = s.split()

    if s == []:
        return [""]

    return s

word = "Robin Singh"
print(string_to_array(word))