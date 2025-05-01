# Given an Integer n, find the reverse of its digits.

# Examples:  

# Input: n = 122
# Output: 221
# Explanation: By reversing the digits of number, number will change into 221.


# Input: n = 200
# Output: 2
# Explanation: By reversing the digits of number, number will change into 2.


# Input: n = 12345 
# Output: 54321
# Explanation: By reversing the digits of number, number will change into 54321.

#Approach 
#Digit extraction and reverse

# 1.Mistake - used simply the method but wrong 


# class Solution:
# 	def reverseDigits(self, n):
# 		# Code here
		
# 		rev=0 
# 		while n>0:
# 		    rev += n% 10 
# 		    n //= 10 
		    
		# return rev
  
  
# 2.Own Code 


# class Solution:
# 	def reverseDigits(self, n):
# 		rev=0 
# 		while n>0:
# 		    rev += rev*10 + n %10  ----------> using += is wrong 
# 		    n //= 10 
		    
# 		return rev


  
#3. Correct Code
class Solution:
  def reverseDigits(self, n):
        rev = 0
        while n > 0:
            rev = rev * 10 + (n % 10)  # Properly shift and add
            n //= 10
        return rev
