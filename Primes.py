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
                                                #by any number but itself, skipping multiples of two
        if n % i == 0:                          #and limiting itself to the square of the number

            return False

    return True

def factors(n):                           #This function finds all the unique prime factors of 
                                                #Any given number
    factors = []

    i = 3

    if n % 2 == 0:

        factors.append(2)
        n = int(n/2)

    while True:

        if prime(i) == True and n % i == 0:

            factors.append(i)

            n = int(n/i)
            i += 2

        else:

            i += 2
        
        if i > n:

            break
          
    return factors



         
            
