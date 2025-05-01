
# Factorial of a Number

# Given the number n (n >=0), find its factorial. Factorial of n is defined as 1 x 2 x … x n. For n = 0, factorial is 1. We are going to discuss iterative and recursive programs in this post.

# Examples:

# Input: n = 5
# Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120


#Wrong

# class Solution:
#     def factorial(self, n):
#         fact = 1
#         return fact*(n-1)



#Correct 

class Solution:
    def factorial(self, n):
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
