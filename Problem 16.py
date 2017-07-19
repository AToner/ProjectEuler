# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

import math

x = math.pow(2, 1000)
string = str(int(x))

result = 0
for c in string:
    result += int(c)

print(result)