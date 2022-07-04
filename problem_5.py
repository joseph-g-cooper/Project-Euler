# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def div_by_all(n):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    for i in nums:
        if n % i != 0:
            return False

    return True

found = False
n = 0

while not found:
    n += 20
    if div_by_all(n):
        break

print(n)