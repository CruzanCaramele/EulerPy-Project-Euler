#If we list all the natural numbers below 10 that are
#multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


def multiples_of_three_and_five(num):

    added_one = 0
    added_two = 0

    for i in range(0, num):
        if i % 3 == 0:
            added_one += i
        
        if i % 5 == 0:
            added_two += i
        
    print added_one + added_two   

multiples_of_three_and_five(1000)
