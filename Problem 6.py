# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

i_sum = 0
i_sum_squared = 0

for i in range(1, 101):
    i_sum += i
    i_sum_squared += i ** 2

difference = (i_sum ** 2) - i_sum_squared

print difference

