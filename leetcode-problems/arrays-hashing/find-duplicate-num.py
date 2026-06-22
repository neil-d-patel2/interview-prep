class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i,x in enumerate(nums):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(x)
            else:
                nums[abs(nums[i]) - 1] *= -1
        
        return -1 
