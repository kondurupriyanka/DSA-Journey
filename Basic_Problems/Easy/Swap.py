# Swap Two Numbers
# Last Updated : 24 Feb, 2025
# Given two numbers a and b, the task is to swap them.

# Examples:

# Input: a = 2, b = 3
# Output: a = 3, b = 2

# Input: a = 20, b = 0
# Output: a = 0, b = 20

# Input: a = 10, b = 10
# Output: a = 10, b = 10 

# Mistake 1 - Swapping using Temp varibale

# temp = a    
# a=b 
# b=a        ----------> b = temp (correct)

#problem - temp = a, a=b, again b=a , no output is correct 
#solution - temp = a,a=b , b = temp ---------correct solution


# use 1 line code a,b=b,a

#2.correct code

class Solution:
    def get(self, a, b):
        #code here
        a,b=b,a
        return a,b

