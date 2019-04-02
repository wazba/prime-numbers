import math
import time
primes = [2]  # Give the first primenumber
str = time.time()

for i in range(2, 100000000):
    for j in range(0, len(primes)):  # Try split number with every previous prime number

        if primes[j] > math.sqrt(i):  # Try if division is positive
            primes.append(i)  # Add the prime number to our list
            print(i)
            break  # Go to next number asap after positive division
        elif i % primes[j] == 0:  # If the division is integer
            break  # Continue to next number

with open('nums.txt', 'w') as f:
    for item in primes:
        f.write("%s\n" % item)
    f.close()

print(time.time() - str)
