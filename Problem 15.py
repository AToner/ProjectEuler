# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# Take a number and produce a string with its value at a given base

# So my dumb way was clearly crazy so time for more "back to basics: math.
# https://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/


def factorial(x):
    result = 1
    for i in range(1, x+1):
        result = result * i

    return int(result)


def square_calcs(x):
    total_moves = 2 * x

    total_possibilities = factorial(total_moves)
    rights = factorial(x)
    downs = rights  # it's a square so the ups and downs are the same

    return int(total_possibilities / rights / downs)


for i in range(1, 21):
    print('There are ', square_calcs(i), ' valid routes for ', i, ' by ', i)

