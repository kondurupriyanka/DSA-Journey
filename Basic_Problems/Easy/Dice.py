# You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.

# Examples:

# Input: n = 2
# Output: 5
# Explanation: For dice facing number 5 opposite face will have the number 2.


# Input: 6 = 6
# Output: 1
# Explanation: For dice facing number 6 opposite face will have the number 1.


#Approach - take real dice check all the numbers opposite directions 

#1. Mistake -- matching with opposite numbers and returning values using return statement 


# class Solution:
#     def oppositeFaceOfDice(self, n):
#     	#code here 
#     	    if n ==1:
#     	        return 6
#     	    elif n ==2:
#     	        return 5
#     	    elif n == 3:
#     	        return 4


#Error getting NONE+ Answer , which means only for 1,2,3 its working and not working for 4,5,6

#2.Corrected Code  - Complete the code chain 

# class Solution:
#     def oppositeFaceOfDice(self, n):
#     	#code here 
#     	    if n ==1:
#     	        return 6
#     	    elif n ==2:
#     	        return 5
#     	    elif n == 3:
#     	        return 4
#     	    elif n ==4:
#     	        return 3 
#     	    elif n ==5 :
#     	        return 2 
#     	    elif n == 6 :
#     	        return 1


# 3.Optimized Solution 

class Solution:
    def oppositeFaceOfDice(self, n):
    	#code here 
    	return 7 - n
 
# Explain - Used the Formula
#the formula to get the opposite face is:

# opposite = 7 - current_face

  	