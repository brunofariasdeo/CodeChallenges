# Write a method sum  that takes an array of numbers and returns the sum of the numbers. 
# The numbers can also be negative. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    total = 0
    for number in a:
        total+= number


    return total

print(sum_array([1, 2, 3]))