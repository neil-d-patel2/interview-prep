'''
index is not recursion depth. It is the first position in the sorted array that the current recursive call is allowed to use. Every recursive call only considers candidates from index onward, ensuring we never reuse earlier elements. The condition i > index tells us we're no longer looking at the first candidate at this recursion level we're looking at a sibling branch. Ifthat sibling has the same value as the previous sibling, it would generate
the exact same combinations, so we skip it. 
'''


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
        
