# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def is_triplet(a, b, c):
    if (a > b) or (b > c): return False
    a_squared = a ** 2
    b_squared = b ** 2
    c_squared = c ** 2

    if (a_squared + b_squared) == c_squared: return True
    return False

target = 1000
for a in range(1, target):
    for b in range(a, target):
        for c in range(b, target):
            if a + b + c > target: break
            if a + b + c == target:
                if is_triplet(a, b, c):
                    print([a, b, c])
                    print([a * b * c])
