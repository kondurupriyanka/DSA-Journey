# You are given two coordinates (x1, y1) and (x2, y2) of a two-dimensional graph. Find the distance between them.

# Examples: 

# Input : x1, y1 = (3, 4)
#            x2, y2 = (7, 7)
# Output : 5

# Input : x1, y1 = (3, 4) 
#            x2, y2 = (4, 3)
# Output : 1.41421

#using formula 

#1. Mistake - not imported Math for round() and not used built in. ------> math.sqrt() 



#2.corrected code

import math

class Solution:
	def distance(self, x1, y1, x2, y2):
		return round(math.sqrt((x1-x2)**2 + (y1-y2)**2))
