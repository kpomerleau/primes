# primes
prime calculator
This code finds the prime factors of any given number. The way it does this is similar to how you would think of a prime factor “tree.” It starts with your given number and attempts to divide it evenly by the first prime number (2). If it can be divided equally 2 is stored. The original number is now thrown out and replaced with the quotient of the original number and the first prime number. Now the next prime number is tested against the new quotient. If it does not evenly divide the new quotient, it is thrown out and the next prime is tested. This goes until a prime that evenly divides is found and stored. This process is repeated until the original number has been divided to be smaller than the next prime number tested.

Suppose we test 100. The first prime tested is 2. 100 is evenly divided by 2 into 50. 2 is stored as a prime factor and we are left with 50. Now 50 is divided by 3. This does not evenly divide, so 3 is thrown out and the next prime is tested: 5. 5 evenly divides 50 into 10. 5 is stored and 50 is replaced with ten. The next two primes are tested (7 and 11). 7 is thrown out because it does not evenly divide 10 and 11 is thrown out because it is greater than 10. This yields the two unique prime factors of 100: 2 and 5.

More notes are in the code itself.
