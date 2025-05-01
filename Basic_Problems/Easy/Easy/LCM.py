# Program to find LCM of two numbers

# LCM of two numbers is the smallest number which can be divided by both numbers. 

# Input :  a = 12, b = 18
# Output :  36
# 36 is the smallest number divisible by both 12 and 18


# Input :  a = 5, b = 11
# Output :  55
# 55 is the smallest number divisible by both 5 and 11


class Solution:
    def lcmAndGcd(self, a: int, b: int) -> list:
        # Helper function to calculate GCD
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        gcd_value = gcd(a, b)
        lcm_value = (a * b) // gcd_value
        return [lcm_value, gcd_value]
