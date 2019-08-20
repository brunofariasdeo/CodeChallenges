def longest_consec(strarr, k):
    dicStrings = {}

    if strarr == [] or k ==0 or k>len(strarr) or k<0:
        return ""
    else: 
        for item in strarr:
            if len(item) in dicStrings.keys():
                dicStrings[len(item)] += [item]
            else:
                dicStrings[len(item)] = [item]

    return stringOutput

print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))