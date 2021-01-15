# Even Fibonacci numbers
# Problem 2
# https://projecteuler.net/problem=2

# Basic example of using a recursion.

def fibonacci(n):
    """
    Find the nth fibonacci number.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # Follow the definition.
        return fibonacci(n - 1) + fibonacci(n - 2)


sum = 0
n = 1

while (fibonacci(n) < 4000000):
    if fibonacci(n) % 2 == 0:
        sum += fibonacci(n)
    n += 1

print(sum)
