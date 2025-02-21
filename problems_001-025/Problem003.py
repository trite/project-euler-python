print('''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

''')

primes, current, target = [2, 3, 5], 7, 600851475143
sqrttar = int(target ** (1/2))
while current <= sqrttar:
    sqrcur = int(current ** (1/2))
    found = False
    for x in primes:
        if (x > sqrcur):
            break
        if (current % x == 0):
            found = True
            break
    if (found == False):
        primes.append(current)
    current += 2
print('Answer: ' + str(max([x for x in primes if target % x == 0])))

# Answer: 6857