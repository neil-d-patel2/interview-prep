'''

15. 3Sum
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000

'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        s = set()
        nums.sort()
        out = []

        
        for i in range(len(nums)):
            L = i + 1
            R = (len(nums)) - 1
            target = nums[i] * -1
            while L < R:
                sum = nums[L] + nums[R]
                if sum < target:
                    L += 1
                elif sum > target: 
                    R -= 1
                else:
                    if (nums[i],nums[L],nums[R]) not in s:
                        out.append([nums[i],nums[L],nums[R]])
                        s.add((nums[i],nums[L],nums[R]))
                    
                    L += 1

        return out



