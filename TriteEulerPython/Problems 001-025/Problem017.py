print('''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

''')

w1 = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
w10 = {0 : 'ten', 1 : 'eleven', 2 : 'twelve', 3 : 'thirteen', 4 : 'fourteen', 5 : 'fifteen', 6 : 'sixteen', 7 : 'seventeen', 8 : 'eighteen', 9 : 'nineteen'}
w20 = {2 : 'twenty', 3 : 'thirty', 4 : 'forty', 5 : 'fifty', 6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}

def numStr(input):
    strIn = str(input)
    result = ''
    while (len(strIn) > 0):
        if (strIn == '1000'):
            result = 'onethousandand'
            break
        elif (len(strIn) == 1):
            if (strIn[0] != '0'):
                result += w1[int(strIn[0])]
        elif (len(strIn) == 2):
            if (strIn[0] != '0'):
                if (strIn[0] == '1'):
                    result += w10[int(strIn[1])]
                    strIn = strIn[1:]
                else:
                    result += w20[int(strIn[0])]
        elif (len(strIn) == 3):
            result = w1[int(strIn[0])] + 'hundredand'
        else:
            return 'ERROR... ' + strIn
        strIn = strIn[1:]
    if (result[-3:] == 'and'):
        result = result[:-3]
    print('{} ({}) = {}'.format(input, len(result), result))
    return result

result = 0
for x in range(1, 1005):
    result += len(numStr(x))

print('Answer: ' + str(result))

print(numStr(1000))





