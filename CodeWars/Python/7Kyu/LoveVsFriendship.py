def words_to_marks(s):
    value = 0

    for letter in s:
        value += ord(letter)-96

    return value

print(words_to_marks('attitude'))