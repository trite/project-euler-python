print('''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

''')

def isPalindrome(inputVal):
    reversed = int((str(inputVal)[::-1]))
    return reversed == inputVal

nMax, nMin, highest = 999, 900, 0
for x in range(nMax, nMin, -1):
    for y in range(nMax, nMin, -1):
        product = x * y
        if ((product > highest) and isPalindrome(product)):
            highest = product
            
print("Answer: " + str(highest))

# Answer: 906609