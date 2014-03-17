# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.

maxValue = 100

def SumOfSquares(nMax):
    return sum([x ** 2 for x in range(1, nMax + 1)])

def SquareOfSums(nMax):
    return sum([x for x in range(1, nMax + 1)]) ** 2

def DiffResult(nMax):
    return SquareOfSums(nMax) - SumOfSquares(nMax)

print("Answer: " + str(DiffResult(maxValue)))