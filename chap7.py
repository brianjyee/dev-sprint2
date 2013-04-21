# Enter your answrs for chapter 7 here
# Name: Brian Yee

import math

# Ex. 7.5
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi():
    k = 0
    est = 0
    a = 2 * math.sqrt(2) / 9801
    term = factorial(4*k) * (1103 + 26390*k)/factorial(k) ** 4 * 396 ** (4*k)
    while term > 1e-15:
        est += (a * term)
        k += 1
        term = (factorial(4*k) * (1103 + 26390*k))/((factorial(k) ** 4) * 396 ** (4*k))
    print k
    return 1/est

#print estimate_pi()
#print math.pi

# How many iterations does it take to converge?
# It appears to have only taken 1 iteration but that doesn't sound right...