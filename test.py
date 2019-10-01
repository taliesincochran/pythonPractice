#!/usr/bin/env python3
import math
def getPrimes(max):
    for n in range(2,max):
        min = math.floor(math.sqrt(n))
        for x in range(min,n):
            if n % x == 0:
                break
        else:
            print(n,'is a prime number')
