# coding=utf-8
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    string = str(n)
    length = len(string)
    result = False
    for c in range(0, length):
        if string[c] != string[length-c-1]:
            break

        if c >= (length-c):
            result = True
            break

    return result


largest = 0
high = 1000
for i in range(0, high):
    for j in range(0, high):
        number = i * j

        # If the number doesn't stand a chance of being the largest, why check for being a palindrome?
        if number > largest:
            if is_palindrome(number):
                largest = number

print(largest)
