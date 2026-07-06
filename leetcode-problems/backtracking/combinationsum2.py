class Solution:
    def combinationSum2(self, candidates, target):
        out = []
        candidates.sort()

        def backtrack(index, path):
            if sum(path) == target:
                out.append(path.copy())
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if sum(path) > target:
                    return
                    
                path.append(candidates[i])
                backtrack(i+1, path)
                path.pop()
            

        backtrack(0, [])
        return out      
        
