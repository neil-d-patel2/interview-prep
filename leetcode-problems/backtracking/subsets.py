class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       out = []

       def backtrack(index, path):
           if index == len(nums):
               out.append(path.copy())
               return 
            
           '''decision 1, include the number in the path'''
           path.append(nums[index])
           backtrack(index + 1, path)
           path.pop()

           backtrack(index + 1, path)


           '''decision 2, do not include the number in the path'''
       backtrack(0, [])
       return out

        





