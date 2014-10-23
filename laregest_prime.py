#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


def largest_prime(num):

    smallest_prime = 2

    while smallest_prime**2 < num:
        
        while num % smallest_prime == 0:
            
            num = num / smallest_prime
            
        smallest_prime += 1
        
    return num

print largest_prime(600851475143)


