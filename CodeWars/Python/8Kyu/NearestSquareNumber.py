def nearest_sq(n):

    if (n**(1/2)) != n: 
        minor = int(n**(1/2))
        higher = int(n**(1/2)) + 1
    
        if (abs((minor**2) - n)) < (abs((higher**2) - n)):
            return (minor**2)
        else:
            return (higher**2)
    else:
        return n

print(nearest_sq(111))