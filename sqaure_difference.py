﻿"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares
of the first ten natural numbers and the square of
the sum is 3025 − 385 = 2640.

Find the difference between the sum of the
squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_squares_diff(num):
    squares = [num**2 for num in range(1,num+1)]
    addition = sum(range(1, num+1)) ** 2

    added_squares = sum(squares)
    
    diff = addition - added_squares

    print diff 
    
    
sum_squares_diff(100)
