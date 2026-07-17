class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()

        def backtrack(index, path):
            print(path)
            if sum(path) == target:
                out.append(path.copy())
                return
            for i in range(index,len(nums)):
                if sum(path) + nums[i] > target:
                    return
                path.append(nums[i])
                backtrack(i,path)
                path.pop()
               

        backtrack(0,[])
        return out

   
