# rogram to print multiplication table of a number
# Last Updated : 13 Feb, 2025
# Given a number n, we need to print its table. 

# Examples : 

# Input:  5
# Output: 
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50


# 1 - Mistake I did

# class Solution:
#     def getTable(self,n):
        
#         for i in range(1,11):
#             return i*n,end=" "  # which end is not written in this way 
        
        #we need to make code return not print so not valid code 
        



#2 - Correct Code 

class Solution:
    def getTable(self,n):
        return [i* n for i in range(1,11)]

#Here RETURN's STATEMENT SYNTAX in Multiple Ways


#1. Returning a single value (like a number, string, or boolean):

# def getAge():
#     return 21  # integer

# def isValid():
#     return True  # boolean

# def greet():
#     return "Hello"  # string


# 2. Returning a list (array):
# def getSquares():
#     return [i**2 for i in range(1, 6)]
# # returns: [1, 4, 9, 16, 25]


# 3. Returning a tuple (multiple values at once):
# def getStats():
#     return (10, 20, 30)
# # Caller can unpack: a, b, c = getStats()


# 4. Returning a dictionary:
# def getUser():
#     return {"name": "Priyanka", "age": 21}


# 5. Returning a function (used in decorators or higher-order functions):
# def outer():
#     def inner():
#         return "I'm inner"
#     return inner  # returns the inner function itself


# 6. Returning nothing (implicitly returns None):
# def sayHello():
#     print("Hello!")
#     # No return → Python adds `return None` behind the scenes


# 7. Returning with a condition:
# def check(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

