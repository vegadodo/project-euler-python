"""
Problem 7.

10001st prime
https://projecteuler.net/problem=7
"""

primes = [2]


def is_prime(num_to_check):
    """Determine if num_to_check is a prime."""
    for prime in primes:
        # We use primes found so far to determine
        # whether num_to_check is a prime.
        # If num_to_check is divisible by any of primes,
        # then num_to_check is not a prime number.
        if num_to_check % prime == 0:
            return False
    return True


current_num = 3
while len(primes) != 10001:
    if is_prime(current_num):
        primes.append(current_num)
    current_num += 1

print(primes[10000])
