# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
# if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
#  though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
#  this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def divisors(x):
    result = []
    for i in range(1, int(x/2)+1):
        if (x % i) == 0:
            result.append(i)
    return result

# Create the abundant numbers
abundant_numbers = []
for n in range(28123, 1, -1):
    number_sum = sum(divisors(n))

    if number_sum > n:
        abundant_numbers.append(n)

# Create all the sums
abn_sums = []
for abn1 in abundant_numbers:
    for abn2 in abundant_numbers:
        abn_sums.append(abn1 + abn2)

# Make the list unique
abn_sums = set(abn_sums)

# Check which numbers aren't in the sums array
result_array = []
for n in range(1, 28123):
    if n not in abn_sums:
        result_array.append(n)

print('Sum = ', sum(result_array))
