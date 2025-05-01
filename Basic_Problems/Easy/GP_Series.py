# Like AP , GP
#GP - Grows MULTIPLIES Repeadly 

#Examples

# "VIP Grows Super Fast"

# Each letter stands for a real-life use of GP:

# V → Virus Spread (doubles/triples fast)

# I → Interest (Compound) (money multiplies)

# P → Population Growth (fast-growing like rabbits 🐇)

# G → Gadget Depreciation (value drops by %)

# S → Signal Strength (reduces with distance)

# F → Followers/Viral Shares (multiplying quickly)

#Common Ratio - r 

class Solution:
    def nthTermOfGP(self, a1: int, a2: int, n: int) -> int:
        r = a2 // a1  
        return a1 * (r ** (n - 1))