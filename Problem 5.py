# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

result = 0
i = 10
while result == 0:

    no_remainder = True
    # Doing it backwards because the divisions will fail quicker, I guess... maybe
    # trying to make brute force less crap
    for div in range(20, 1, -1):
        test = float(i) / float(div)
        if not test.is_integer():
            no_remainder = False
            break

    if no_remainder:
        result = i

    i += 1

print(result)
