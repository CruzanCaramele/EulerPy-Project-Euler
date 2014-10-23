"""
2520 is the smallest number that can
be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that
is evenly divisible by all of the numbers from 1 to 20?
"""

def small_helper(number, num):
    for n in reversed(range(1, num+1)):
        if number % n != 0:
            return False
    return True

def smallest_multiple(num):
    if num < 1:
        return False
    elif num == 1:
        return 1
    else:
        hop = smallest_multiple(num-1)
        number = 0
        found = False
        while not found:
            number += hop
            found = small_helper(number, num)
        return number

print smallest_multiple(20)
    

    

