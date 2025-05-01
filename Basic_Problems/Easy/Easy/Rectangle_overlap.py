# Find if two rectangles overlap

# Given two rectangles, find if the given two rectangles overlap or not.
# Note that a rectangle can be represented by two coordinates, top left and bottom right. So mainly we are given following four coordinates. 
# l1: Top Left coordinate of first rectangle. 
# r1: Bottom Right coordinate of first rectangle. 
# l2: Top Left coordinate of second rectangle. 
# r2: Bottom Right coordinate of second rectangle.a

class Solution:
    def doOverlap(self, L1, R1, L2, R2):
        # If one rectangle is to the left of the other
        if L1[0] > R2[0] or L2[0] > R1[0]:
            return 0
        
        # If one rectangle is above the other
        if R1[1] < L2[1] or R2[1] < L1[1]:
            return 0
        
        return 1  # Rectangles overlap
