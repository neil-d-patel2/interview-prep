'''

Longest Consecutive Sequence
Medium
Topics
Company Tags
Hints
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

nums=[9,1,4,7,3,-1,0,5,8,-1,6]

expected 7
output 9 

nums =
[1,2,6,7,8]

Use Testcase
Output
2
Expected
3
''' 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        s = set(nums)
        sorted_nums = list(s)        
        
        sorted_nums.sort()
        total_cons = 1
        list_of_totals = []
        for x in range (len(sorted_nums) - 1):

            if sorted_nums[x] + 1 == sorted_nums[x + 1]:
                total_cons += 1
            else:
                list_of_totals.append(total_cons)
                total_cons = 1
        
        list_of_totals.append(total_cons)
        largest = max(list_of_totals)
        return largest
