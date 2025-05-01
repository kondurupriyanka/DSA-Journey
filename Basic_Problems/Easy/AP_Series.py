#Approach 
#Maths Formula 
#Using for ADDING Repeadly

# Nth term of AP from First Two Terms
# Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively, the problem is to find the nth term of the series. 
# Examples :
# Input : a1 = 2,  a2 = 3,  n = 4
# Output : 5
# Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5. 

# Input : a1 = 1, a2 = 3, n = 10
# Output : 19
# Explanation:  The series is: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21..... Thus,10th term is 19.

#Examples
# S → Salary Hike (fixed increase)

# A → Age Gaps (siblings with same age difference)

# F → Fare Increases (like cab meter + ₹10/km)

# E → Equal Installments (EMI, rent increase)

# Stairs → Steps increase height by same inches

class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        
        d = a2 - a1 
        return a1 + (n - 1)* d
        
