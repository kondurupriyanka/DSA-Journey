# Program for Square Root of Integer
# Last Updated : 14 Feb, 2025
# Given a positive integer n, find its square root. If n is not a perfect square, then return floor of √n.

# Examples : 

# Input: n = 4
# Output: 2
# Explanation: The square root of 4 is 2.


# Input: n = 11
# Output: 3
# Explanation: The square root of 11 lies in between 3 and 4 so floor of the square root is 3.

#1.Wrong ans

# import math
# class Solution:
#     def floorSqrt(self, n): 
    
#         a=math.sqrt(n)
#         if n==a:
#              return a 
#         else:
#              return round(a)



#2.Correct code

import math

class Solution:
    def floorSqrt(self, n): 
        return int(math.sqrt(n))
       
       # return floor(math.sqrt(n))
       
       
       
#INT and FLOOR gives same Output 


#WHY gives same value and whts the use to make create them 1 is enough no if gives same ouput 

# The answer lies in the purpose and behavior across all inputs, not just positive numbers.


# Let's compare with real examples:
# Case 1: Positive number

# >>> int(4.9)
# 4
# >>> math.floor(4.9)
# 4
# ➡ Same result ✅


# Case 2: Negative number
# python
# Copy
# Edit
# >>> int(-4.9)
# -4
# >>> math.floor(-4.9)
# -5
# ➡ Different result ❌



# 🧠 In short:
# int() is for type conversion and truncating decimals (toward 0).

# math.floor() is for mathematics, where floor means down, even into more negative numbers.


      
    
    
