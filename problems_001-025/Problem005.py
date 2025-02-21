print('''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

''')

nMax = 20
nSec = nMax - 1
nStep = nMax * nSec
current = nStep

def isMultiple(testValue, fMax):
    for x in range(fMax, 2, -1):
        if testValue % x != 0:
            return False
    return True

while(not(isMultiple(current, nMax))):
    current += nStep

print("Answer: " + str(current))

# Answer: 232792560