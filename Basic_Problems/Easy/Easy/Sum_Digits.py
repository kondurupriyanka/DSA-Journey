# Given a number n, find the sum of its digits.

# Examples : 

# Input: n = 687
# Output: 21
# Explanation: The sum of its digits are: 6 + 8 + 7 = 21


# Input: n = 12
# Output: 3
# Explanation: The sum of its digits are: 1 + 2 = 3


#Approach : I think using len() and same as sum code 

#Wrong code:len only works with strings , arrays (not integer , float) ---> a=456, 4+5+6

# class Solution:
#     def sumOfDigits (self, n):
#         # code here
#         length = len(n)
#         tot=0
#         for i in range(length):
#             tot+= i 
        
#         return tot    

#2. Use Digit Extraction

# n % 10 → extracts the last digit of the number.

# n // 10 → removes the last digit from the number.

# Repeating this in a loop allows you to process each digit individually from right to left.

#code

class Solution:
    def sumOfDigits(self, n):
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total


# ▶ Step-by-Step Execution for n = 123
# Iteration	n	n % 10 (last digit)	total (sum so far)	n // 10 (remove last digit)
# 1	123	3	0 + 3 = 3	12
# 2	12	2	3 + 2 = 5	1
# 3	1	1	5 + 1 = 6	0
# 4	0	loop ends	final result = 6