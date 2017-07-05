# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def is_even(number):
    return number % 2 == 0


def chain_count(number):
    count = 0
    while number > 1:
        count += 1
        if is_even(number):
            number = number / 2
        else:
            number = (3 * number) + 1

    return count + 1

longest_chain_count = 0
longest_chain_value = 0
for number in range(2, 1000000):
    count = chain_count(number)
    if count > longest_chain_count:
        longest_chain_count = count
        longest_chain_value = number

print([longest_chain_count, longest_chain_value])
