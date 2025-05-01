# Program to find sum of first n natural numbers
# Last Updated : 07 Mar, 2025
# Given a number n, find the sum of the first n natural numbers.

# Examples : 

# Input: n = 3
# Output: 6
# Explanation: Note that 1 + 2 + 3 = 6

# Input  : 5
# Output : 15 
# Explanation : Note that 1 + 2 + 3 + 4 + 5 = 15


#1. My Mistake

#Remember Formula - n*(n+1)//2 --------> Time,Space Compleixty o(1), o(1)

#Beginner learning use Total or sum 


# class Solution:
#     def seriesSum(self, n : int) -> int:
#         for i in range(n):
#             return i+n -----no sense
        

#2. Correct Code 
class Solution:
    def seriesSum(self, n : int) -> int:
        
        for i in range(n):
            return n*(n+1)//2
        
        # total = 0
        # for i in range(1, n + 1):
        #     total += i
        # return total
        
