# Given a number n, determine whether it is a prime number or not.

# A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

# Examples :

# Input: n = 7
# Output: true
# Explanation: 7 has exactly two divisors: 1 and 7, making it a prime number.
# Input: n = 25
# Output: false
# Explanation: 25 has more than two divisors: 1, 5, and 25, so it is not a prime number.
# Input: n = 1
# Output: false
# Explanation: 1 has only one divisor (1 itself), which is not sufficient for it to be considered prime.

#Approach 

# 🧠 Easy-to-Remember Prime Check Logic
# ✅ If number is 1 or less → Not Prime
# (1 is not prime)

# ✅ If number is 2 → Prime
# (2 is the only even prime number)

# ✅ If number is even (but not 2) → Not Prime
# (Because it’s divisible by 2)

# ✅ Check for odd divisors from 3 up to √n

# If any number divides n → ❌ Not Prime

# If none divide → ✅ Prime

# ✨ Simple Rule Summary:
# “Check if it’s divisible by any number from 2 to √n.”
# – If YES → Not Prime
# – If NO → Prime


#1.Mistake - Wrong code -- 5/1000 cases passed , using divisbile condition
# class Solution:
#     def isPrime(self, n):
#         # code here
#         if n%1==0 :
#             return False
#         else:
#             return True


#2. Correct code 

import math

class Solution:
    def isPrime(self, n):
        if n<=1:
            return True 
        elif n==2:
            return False
        elif n%2==0:
            return False
        for i in range(3,math.sqrt(n)+1,2):
            if n%i==0:
                return False
        return True    
    
    
#logic remember
# Prime Number Check - Simple Logic to Remember
# Step 1: Handle Small Numbers First

# If n <= 1, return False (1 is not prime, and no number less than 1 is prime).

# If n == 2, return True (2 is the only even prime number).

# Step 2: Eliminate Even Numbers

# If n is even and not equal to 2, return False (because all even numbers greater than 2 are not prime).

# Step 3: Check Divisibility

# Check if n is divisible by any number from 3 to √n.

# Why √n? Because if n is divisible by some number greater than √n, the corresponding smaller factor will already have been checked.

# If any number divides n perfectly (n % i == 0), return False (since n is not prime).


#Using Square Root becz to not get checking all (1,2) or (2,1) to avoid and maintain optimized we use this 

    