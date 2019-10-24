# Link: https://www.codewars.com/kata/histogram-h1/train/python

def histogram(results):
    histogramList = []

    for index, number in enumerate(reversed(results)):
        if number != 0:
            histogramList.append(str(abs(index-(len(results)))) + "|" + number*"#" + " " + str(number))
        else:
            histogramList.append(str(abs(index-(len(results)))) + "|")
    
    print(histogramList)
    return '\n'.join(histogramList)

print(histogram([7,3,10,1,0,5]))