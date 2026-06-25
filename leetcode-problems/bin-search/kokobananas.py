'''

Notes: 

-When doing a binary search, try to find bounds for your answer (sorted)
-For this question specificially, setting L = 0 instead of 1 was the biggest issue even tho its small in hindsight
-Understand when/how to track your end result output

'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        L = 1 
        R = max(piles)
        out = R

        while L <= R:
            out = 0 
            k = (L + R) // 2
            for x in piles:
                out += math.ceil(float(x) / k)

            if out <= h:
                res = k
                R = k - 1
            else:
                L = k + 1 
    
        return res
