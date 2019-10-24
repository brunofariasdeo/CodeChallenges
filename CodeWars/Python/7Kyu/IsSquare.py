def is_square(n):    
    if (n**(1/2)) == int(abs(n**(1/2))):
        return True
    else:
        return False # fix me

print(is_square(25))