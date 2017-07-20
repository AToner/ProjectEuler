# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
import math

single_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teen_words = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen']
tens_words = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def words_for(x):
    if x == 1000:
        return 'one thousand'

    hundreds = int(math.floor(x / 100))

    result = ''
    if hundreds > 0:
        result += single_words[hundreds - 1] + ' hundred'
        x -= hundreds * 100
        if x > 0:
            result += ' and '

    if 1 <= x < 10:
        result += single_words[x - 1]
        x = 0
    elif 10 <= x <= 19:
        result += teen_words[x - 10]
        x = 0
    elif x >= 20:
        tens = int(math.floor(x / 10))
        result += tens_words[tens - 2]
        x -= tens * 10

    if x > 0:
        result += ' ' + single_words[x - 1]

    return result

result = 0
for i in range(1, 1001):
    result += len(words_for(i).replace(' ', ''))

print(result)
