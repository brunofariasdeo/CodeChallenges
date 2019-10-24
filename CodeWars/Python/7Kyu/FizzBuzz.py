def fizzbuzz(n):
    fizzBuzzList = []

    for number in range(1,n+1):
        if number % 3 == 0:
            if number % 5 == 0:
                fizzBuzzList.append("FizzBuzz")
            else:
                fizzBuzzList.append("Fizz")
        elif number % 5 == 0:
            if number % 3 == 0:
                fizzBuzzList.append("FizzBuzz")
            else:
                fizzBuzzList.append("Buzz")
        else:
            fizzBuzzList.append(number)

    return fizzBuzzList

print(fizzbuzz(10))