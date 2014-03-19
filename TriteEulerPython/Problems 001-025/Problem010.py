print('''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

''')

primes, currentPrime, target = [2, 3, 5], 7, 2000000
while currentPrime < target:
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
    currentPrime += 2
print('Answer: ' + str(sum(primes)))

# Answer: 142913828922