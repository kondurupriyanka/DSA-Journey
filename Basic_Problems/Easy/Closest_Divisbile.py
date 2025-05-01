# Given two integers n and m. The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.

# Examples :

# Input: n = 13 , m = 4
# Output: 12
# Explanation: 12 is the Closest Number to 13 which is divisible by 4.
# Input: n = -15 , m = 6
# Output: -18
# Explanation: -12 and -18 are both similarly close to -15 and divisible by 6. but -18 has the maximum absolute value. So, Output is -18

#Approach 

# You are given two integers:

# n → a number (can be negative or positive)

# m → a divisor

# 🔸 Goal:
# Find the number closest to n that is divisible by m.

# If there are two equally close numbers, return the one with higher absolute value (i.e., further from zero).

# Input: n = 13, m = 4
# Multiples of 4: ... 4, 8, 12, 16, 20 ...
# Which are near 13? → 12 and 16

# Distance from 13 →

# |13 - 12| = 1

# |13 - 16| = 3
# ✅ 12 is the closest, so output is 12.


#  Example 2:
# Input: n = -15, m = 6
# Multiples of 6: ... -18, -12, -6, 0, 6 ...
# Which are close to -15? → -12 and -18

# Both are at a distance of 3 →

# |-15 - (-12)| = 3

# |-15 - (-18)| = 3
# ✅ But -18 has higher absolute value (|-18| > |-12|)
# → So output is -18.

# class Solution:
#     def closestNumber(self, n, m):
#         q = round(n / m)
#         return m * q
    
    
# round() — What it Does:
# round(x) rounds a number x to the nearest integer.

# If it's exactly in the middle (like 2.5), Python uses round half to even (so round(2.5) = 2, round(3.5) = 4).

# 🔹 Why Use round(n/m)?
# This gives us the closest integer multiple of m to n.

# Example:

# n = 13, m = 4
# n/m = 3.25
# round(3.25) = 3
# 3 * 4 = 12



#round(2.5) = 2, round(3.5) = 4).

# why 1 gives less and other upper value


# Round Half to Even" Rule
# Also known as Banker's Rounding


# What does it mean?
# When a number ends in .5, Python rounds to the nearest even number.

# Value	round() Result	Why?
# 2.5	2	2 is even
# 3.5	4	4 is even
# 4.5	4	4 is even
# 5.5	6	6 is even


#Working code

class Solution:
    def closestNumber(self, n, m):
        q = n // m
        n1 = m * q
        n2 = m * (q + 1)

        if abs(n - n1) < abs(n - n2):
            return n1
        elif abs(n - n1) > abs(n - n2):
            return n2
        else:
            # When both are equally close
            return n1 if abs(n1) > abs(n2) else n2


