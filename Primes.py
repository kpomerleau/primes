#Finds the unique Prime Factors of any given number

#Define functions:

    #Is Prime
        #first, test whether the number is 1 or 0 (which are most definitely not
            #primes
        #second, tests whether the number is divisible by any number besides itself
            #from 2 to the number in question
        #if it fails both tests, the number is a prime number

def prime(n):

    if n == 1 or n == 0:                        #1 and 0 are not primes

        return False

    if n > 2 and n % 2 == 0:                    #Any even number greater than 2 is not a prime

        return False

    for i in range(3, (int(n**0.5) + 1), 2):    #Checks whether a number is divisible
                                                #by any number 
        if n % i == 0:

            return False

    return True

def factorization(n):

    factors = []

    x = 0
    i = 3

    if n % 2 == 0:

        factors.append(2)

        x += 1

    while(True):

        if prime(i) == True and n % i == 0:

            factors.append(i)

            n = n/i
            x += 1
            i += 2

            if i > n:

                False

        i += 2
          
    return factors


         
            
