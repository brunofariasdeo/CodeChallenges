def timeConversion(s):
    timeList = s[:-2].split(":")

    if s[-2:] == "PM" and timeList[0] != "12":
        timeList[0] = str(int(timeList[0]) + 12)
    elif s[-2:] == "AM" and timeList[0] == "12":
        print("a")
        timeList[0] = "00"

    return ':'.join(timeList)

print(timeConversion("12:40:22AM"))