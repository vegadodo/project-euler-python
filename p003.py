"""
Problem 3.

Largest prime factor
https://projecteuler.net/problem=3
"""


def is_prime(n):
    """Determine whether the given integer n is prime."""
    result = True
    for i in range(n - 1, 2, -1):
        if n % i == 0:
            # If n is divisible by a smaller integer, then n is not prime.
            result = False
            break

    return result


# Initial value (which is never meant to be the final answer!)
largest_prime = 1

current_number = 2

# We only need to check for numbers smaller than sqrt(600851475143)
# However, we will not use sqrt() function!
# We can just compare the quotient with the divisor.

while 600851475143 // current_number >= current_number:
    # We first check if current_number can divide 600851475143.
    # If 600851475143 is divisible
    # then we check if current_number is a prime, with the help of is_prime(n).
    if 600851475143 % current_number == 0 and is_prime(current_number):
        largest_prime = current_number
    current_number += 1

print(largest_prime)
