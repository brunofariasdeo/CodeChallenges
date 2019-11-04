def loops(n):
    output = []

    for number in range(1,11):
        result = n*number
        output.append(str(n) + " x " + str(number) + " = " + str(result))
    
    return '\n'.join(output)

print (loops(2))
