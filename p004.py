# Largest palindrome product
# Problem 4
# https://projecteuler.net/problem=4

def is_palindrome(n):
    """
    Find if n is palindrome.
    """

    # Convert the given number into list.
    number_original = list(map(int, str(n)))

    # First, store a copy of the list of original number.
    number_reversed = number_original[:]
    # Then, reverse the list.
    number_reversed.reverse()

    return (number_original == number_reversed)


def is_prod_of_two_3_digit_num(n):
    """
    Find if n is the product of 3-digit numbers.
    """

    result = False

    for i in range(100, 1000):
        if n % i == 0 and n // i in range(100, 1000):
            result = True
            break

    return result


# Initial value (which is never meant to be the final answer!)
largest_palindrome = 1

for i in range(999999, 10000, -1):
    if is_palindrome(i) and is_prod_of_two_3_digit_num(i):
        largest_palindrome = i
        break

print(largest_palindrome)
