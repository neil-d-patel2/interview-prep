'''
Longest Substring Without Repeating Characters
Medium
Topics
Company Tags
Hints
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"  

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        L = 0
        R = L + 1
        sset = set()
        sset.add(s[L])
        maxLen = 1

        while R < len(s):
            if s[R] not in sset:
                sset.add(s[R])
                R += 1
                if len(sset) > maxLen:
                    maxLen = len(sset)
            else:
                L += 1
                R = L + 1
                sset.clear()
                sset.add(s[L])


        return maxLen


             
