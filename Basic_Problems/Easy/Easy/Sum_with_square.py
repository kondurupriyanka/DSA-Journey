   
# Sum of Squares of First n Natural Numbers
# Given an integer n. The task is to calculate the sum of the squares of the first  n natural numbers.

# Examples:

# Input: n = 2
# Output: 5
# Explanation: 12 + 22 = 5
# Input: n = 3
# Output: 14
# Explanation: 12 + 22 + 32 = 5
# Constraints:
# 0 <= n <= 103
   
   
 #1.wrong code 
 
#  total=0 
        
# while number>0:
#     number += number%10 
#     number//10 
            
# return total**2 
  
  
  #2. corrected code
    # def sumOfSquares(self, number):
    #     total = 0
    #     i = 1
    #     while i <= number:
    #         total += i * i
    #         i += 1
    #     return total
    
 #3.optimized code using formula 
 
class Solution:
    def sumOfSquares(self, number):
        return (number * (number + 1) * (2 * number + 1)) // 6
   