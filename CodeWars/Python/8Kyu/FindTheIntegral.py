def integrate(coefficient, exponent):
    return (str(int(coefficient/(exponent+1))) +"x^" + str(exponent+1))

print(integrate(3,2))