"""
Problem 2.

Even Fibonacci numbers
https://projecteuler.net/problem=2
"""

fibonacci_whole = [1, 2]
fibonacci_even = [2]

while fibonacci_whole[-1] < 4000000:
    # Using the definition, first find the next fibonacci number
    # by adding last two fibonacci numbers.
    next_fibonacci = sum(fibonacci_whole[-2:])

    fibonacci_whole.append(next_fibonacci)

    # If new fibonacci number is even, we also append this to
    # the list of even fibonacci numbers.
    if next_fibonacci % 2 == 0:
        fibonacci_even.append(next_fibonacci)

print(sum(fibonacci_even))
