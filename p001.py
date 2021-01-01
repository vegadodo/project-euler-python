# Multiples of 3 and 5
# Problem 1
# https://projecteuler.net/problem=1

sum = 0

# Pretty self-exlanatory code.
# Check if given number is dividable by 3 or 5.
# Rinse and repeat for 1 to 1000.

for i in range (1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i

print(sum)
