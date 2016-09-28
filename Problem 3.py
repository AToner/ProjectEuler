# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


target = 600851475143
#target = 13195
current = target
factors = []

done = False
while current > 0:
    largest = 0
    for i in gen_primes():
        # Find a prime that divides into the number
        check = float(current) / float(i)
        if check.is_integer():
            largest = i

        # Do we think they'll be a bigger number that will divide into the number?
        if i > (current / i):
            if largest != 0:
                factors.append(largest)
                current = current / largest
            else:
                current = 0
            break

print max(factors)
