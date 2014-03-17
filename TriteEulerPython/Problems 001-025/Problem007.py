# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

primes, currentPrime, largest, currentCount, target = [2, 3, 5], 5, 7, 3, 10001
while currentCount <= target:
    sqrcur = int(currentPrime ** (1/2))
    found = False
    for x in primes:
        if (x > sqrcur):
            break
        if (currentPrime % x == 0):
            found = True
            break
    if (found == False):
        primes.append(currentPrime)
        largest = currentPrime
        currentCount += 1
    currentPrime += 2
print(largest)