'''

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.lengt

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)

        count = defaultdict(int)
        out = 0 

        L = 0 


        for R in range(len(s)):
                count[s[R]] += 1
                max_key = max(count, key=count.get)
                total_sum = sum(value for key, value in count.items() if key != max_key)

                if total_sum <= k and total_sum + count[max_key] > out:
                    out = total_sum + count[max_key]
                else: 
                    L += 1

        return out 


            

            
