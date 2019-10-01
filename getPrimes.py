#!/usr/bin/env python3
import math
import sys
answer = ""
def getPrimes(max):
    for n in range(2,max):
        max = math.floor(math.sqrt(n))
        for x in range(2, max):
            if n % x == 0:
                break
        else:
            print(n)
x = int(input("Find all primes below... "))

getPrimes(x)






