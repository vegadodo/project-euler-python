"""
Problem 6.

Sum square difference
https://projecteuler.net/problem=6
"""

# Pretty self explanatory.

sum_of_square = sum(i ** 2 for i in range(101))
square_of_sum = sum(range(101)) ** 2

answer = square_of_sum - sum_of_square

print(answer)
