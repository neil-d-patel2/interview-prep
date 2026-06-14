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
        sset = set()
        L = 0
        maxLen = 0

        for _ in range(len(s)):
            while s[R] in sset:
                sset.remove(s[L])
                L += 1
            
            sset.add(s[R])
            maxlen = max(maxLen, R - L + 1)

        return maxLen


             
