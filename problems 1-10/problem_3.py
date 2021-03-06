# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
factors = []
d = 2

while n > 1:
    while n % d == 0:
        factors.append(d)
        n /= d

    d += 1

    if d * d > n:
        if n > 1: factors.append(n)
        break

print(max(factors))