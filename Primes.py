#Finds the unique Prime Factors of any given number. It uses a method similar to using a factor tree.
#It takes your number and divides it first by the smallest possible prime factor. It then saves that factor.
#Then it looks for the next lowest prime factor of the quotient N divided by the previous prime factor.
#The code works quickly, until you get into numbers with 18-20 digits. Then it takes about 4 seconds.

#Function 1 defines primes.

def prime(n):

    if n == 1 or n == 0:                        #1 and 0 are not primes

        return False

    if n > 2 and n % 2 == 0:                    #Any even number greater than 2 is not a prime

        return False

    for i in range(3, (int(n**0.5) + 1), 2):    #Checks whether a number is divisible
                                                #by any number but itself, skipping multiples of two
        if n % i == 0:                          #and limiting itself to the square root of the number

            return False

    return True

#Function 2 finds prime factors.

def factors(n):                                 #This function finds all the unique prime factors of 
                                                #Any given number and saves it into an array
    factors = []

    i = 3

    if n % 2 == 0:                              #Starts with 2 (the only even prime). If the number is divisible 
                                                #by 2, put 2 in an array. Then divide n by 2
        factors.append(2)

        n = int(n/2)

    while True:

        if prime(i) == True and n % i == 0:     #Tests whether any given odd number (starting at 3) is both prime
                                                #and a factor of n (or n divided by the previous factor).
            factors.append(i)

            n = int(n/i)
            i += 2

        else:

            i += 2
        
        if i > n:                               #once you get to an i that is greater than n, you have exhausted all
                                                #possible factors (by definition)
            break
          
    return factors

answer = max(factors(600851475143))

print(answer)
         
            
