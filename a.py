Contains Duplicate:

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

    s = set(nums)

    return len(s) < len(nums)   



Two sum:

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Notes, look over every element, if a new element + an 
        # existing one creates the target, return both indexes.

        h = {}

        for i,x in enumerate(nums):
            if target - x in h:
                return [h[target-x],i] 
            else:
                h[x] = i

        return []

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
