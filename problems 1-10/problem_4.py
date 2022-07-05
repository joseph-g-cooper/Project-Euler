# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    s = [x for x in str(n)]
    sr = [str(n)[-(x + 1)] for x in range(len(str(n)))]
    if s == sr:
        return True
    return False

largest = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if is_palindrome(i * j):
            if (i * j) > largest:
                largest = i * j
                
print(largest)