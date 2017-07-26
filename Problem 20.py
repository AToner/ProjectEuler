# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(x):
    result = 1
    for i in range(1, x+1):
        result = result * i

    return int(result)

result = 0
for c in str(factorial(100)):
    result += int(c)

print(result)
