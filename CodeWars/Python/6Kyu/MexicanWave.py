# Link: https://www.codewars.com/kata/mexican-wave/train/python

def wave(str):
    waveList = []
    str = list(str.lower())

    for index, item in enumerate(str):
        if item is not " ":
            str[index] = item.upper()
            waveList.append(''.join(str))
            str[index] = item.lower()
    return waveList

print(wave("Hello"))