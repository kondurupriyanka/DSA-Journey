
# GCD of two numbers
# Difficulty: BasicAccuracy: 51.03%Submissions: 110K+Points: 1
# Given two positive integers a and b, find GCD of a and b.

# Note: Don't use the inbuilt gcd function

# Examples:

# Input: a = 3, b = 6
# Output: 3
# Explanation: GCD of 3 and 6 is 3
# Input: a = 1, b = 1
# Output: 1
# Explanation: GCD of 1 and 1 is 1


class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
