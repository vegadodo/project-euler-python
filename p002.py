"""
Problem 2.

Even Fibonacci numbers
https://projecteuler.net/problem=2
"""

# Basic example of using a recursion.


def fibonacci(n):
    """Return the nth fibonacci number."""
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Follow the definition.
    return fibonacci(n - 1) + fibonacci(n - 2)


answer = 0
n = 1

while fibonacci(n) < 4000000:
    if fibonacci(n) % 2 == 0:
        answer += fibonacci(n)
    n += 1

print(answer)
