class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        h = {}
        for ch in s:
            if ch not in h:
                h[ch] = 0
            else:
                h[ch] += 1

        # now we have the number of items in k
        # we want to get the max of them 
       
