#A palindromic number reads the same both ways.
#The largest palindrome made from the product of
#two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

number = range(100, 999)
def largest_palindrome(number):

    for n in number:
        result = str(n * n)
        if result[0:-1] == result[-1:0:-1]:
            print result

            
            
                
                
            
            
                
                
            
            
            
            
                
        

    

        


largest_palindrome(number)
