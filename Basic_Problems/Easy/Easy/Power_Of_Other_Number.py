# Check if a number is a power of another number

# Given two positive numbers x and y, check if y is a power of x or not.
# Examples : 

# Input:  x = 10, y = 1
# Output: True
# x^0 = 1


# Input:  x = 10, y = 1000
# Output: True
# x^3 = 1


# Input:  x = 10, y = 1001
# Output: False


class Solution:
    def isPowerOfAnother(self, x, y):
        if x == 1:  # Special case: if x is 1, only 1^k = 1 for any k
            return y == 1  # So if y is also 1, it's True, else False

        if y == 1:  # Any number raised to power 0 is 1, so return True if y = 1
            return True
        
        while y % x == 0:  # While y is divisible by x
            y //= x  # Divide y by x
        
        return y == 1  # If y becomes 1, it's a power of x, else it's not