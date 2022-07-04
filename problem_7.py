# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

n = 1
counter = 0

while counter < 10001:
    n += 1

    # Determine if divisible by another number, if so n is not prime
    for i in range(2, n + 1):
        if n % i == 0:
            break

    if i == n:
        counter += 1

print(n)