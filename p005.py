# Smallest multiple
# Problem 5
# https://projecteuler.net/problem=5

# For integer a, b, it holds that
# a * b = LCM(a, b) * GCD(a, b).
# Starting from range(1, 21), we replace two head elements x, y to LCM(x, y).

def gcd(a, b):
    """
    Find the greatest common divisor of two integers a, b.
    This uses Euclid's algorithm.
    """
    dividend = max(a, b)
    divisor = min(a, b)

    if divisor == 0:
        return dividend
    else:
        return gcd(dividend % divisor, divisor)


lcm_list = range(1, 21)

while len(lcm_list) != 1:
    lcm_head = (lcm_list[0] * lcm_list[1]) / gcd(lcm_list[0], lcm_list[1])
    del lcm_list[0:2]
    lcm_list.insert(0, lcm_head)

print(lcm_list[0])
