# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt


for a in range(0, 333):
    for b in range(a + 1, 500):
        c = sqrt((a ** 2) + (b ** 2))

        if a + b + c == 1000:
            print(a, b, c)
            product = a * b * c
            print(product)
            exit(0)