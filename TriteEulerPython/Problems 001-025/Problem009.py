'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

found = False

# if C is 334 then B must be 333 or less and A must be 332 or less, 334+333+332 = 999
# C cannot be larger than 997 and still have valid A/B values to end up under 1000
for c in range(334, 997):
    if found == False:
        # if C must be 334 or larger then the largest B can be is 665 as 665+1+334 = 1000
        for b in range(2,665):
            if found == False:
                # if A is 333 then B must be at least 334 and C at least 335, 333+334+335 = 1002
                for a in range(1, 332):
                    if found == False and a < b < c:
                        if (1000 == a + b + c) and (a ** 2 + b ** 2 == c ** 2):
                            found = True
                            print('Answer: ' + str(a * b * c))
                            print('A, B, C: {} {} {}'.format(a, b, c))
                    else:
                        break
            else:
                break
    else:
        break
    
# Answer: 31875000
# A, B, C: 200 375 425