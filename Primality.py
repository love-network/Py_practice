#!/usr/bin/env python

#--------------------------------------#
#The minor modification
#--------------------------------------#

def get_integer():
    return int(raw_input("Please enter a number: "))

def primality(num):
    if num <= 1:
        print("Invalid input")
    else:
        primes = range(2,(num-1))
        count_prim = 0
        for i in primes:
            if num % i == 0:
                count_prim += 1
        if count_prim == 0:
            print("This is a prime")
        else:
            print("This is not a prime")

#Main function
num = get_integer()
primality(num)
