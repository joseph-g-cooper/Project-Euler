# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

n = 2000000

primes_sum, sieve_arr = 0, [True] * n

for p in range(2, n):
    if sieve_arr[p]:
        primes_sum += p

        for i in range(p*p, n, p):
            sieve_arr[i] = False

print(primes_sum)

# This algorithm makes use of Sieve of Eratosthenes
# This sieve is an efficient algorithm for finding primes in a given range