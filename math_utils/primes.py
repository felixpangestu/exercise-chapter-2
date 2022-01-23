from math import sqrt, floor

def isprime(n):
    y = floor(sqrt(n)) 

    if n == 1:
        return False
        
    for i in range(2,y+1):
        if n%i == 0:
            return False
    return True