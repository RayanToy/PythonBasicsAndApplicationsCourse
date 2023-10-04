import math
def primes():
    a = 2
    while True:
        if (math.factorial(a-1) + 1) % a == 0:
            yield a
        a += 1