Is anagram:

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter

***IMPORTANT NOTE***

Counter is an object from collections that can immediately get the count of chars in a string, or words in an array, etc. 

They also have an equality function as well as you can see in the return statement. 
