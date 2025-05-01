# Check whether triangle is valid or not if sides are given
# Last Updated : 10 Feb, 2025
# Given three sides, check whether triangle is valid or not. 

# Examples:  

# Input :  a = 7, b = 10, c = 5 
# Output : Valid
# We can draw a triangle with the given three edge lengths.

# Input : a = 1, b = 10, c = 12 
# Output : Invalid
# We can not draw a triangle with the given three edge lengths. 


# Approach: A triangle is valid if sum of its two sides is greater than the third side. If three sides are a, b and c, then three conditions should be met. 

# (a + b) > c
# (a + c) > b
# (b + c) > a  

# class Solution:
#     def checkValidity(self, a: int, b: int, c: int) -> bool:
#         # code here
#         if (a+b)>c :
#             return "Valid"
#         elif (b+c)>a :
#             return "Valid"
#         elif (a+c)>b:
#             return "Valid" 
            
        # else:
        #     return "Invalid"
        
        
        
#2. Corrected Code

#User function Template for python3
class Solution:
    def checkValidity(self, a: int, b: int, c: int) -> bool:
        # code here
            
        if (a + b > c) or (a + c > b) or (b + c > a):
            return "Valid"
        else:
            return "Invalid"    
        

