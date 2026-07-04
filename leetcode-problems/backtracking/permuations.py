'''
out = []
permutation = [1,2,3]

if not used[0], not at used[1] , not at used [2]
'''



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        out = []
        permutation = []
        used = defaultdict(lambda: False)

        def backtrack(out, nums, permutation, used):
            if(len(permutation) == len(nums)):
                out.append(permutation.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    permutation.append(nums[i])
                    backtrack(out, nums, permutation, used)
                    used[i] = False
                    permutation.pop() 

        
        backtrack(out, nums, permutation, used)
        return out
