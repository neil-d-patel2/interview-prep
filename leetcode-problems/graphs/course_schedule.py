from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
             
        ''' maps a number to its prerequisites'''
        visiting = set()
        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visiting:
                return False
            
            visiting.add(preMap[crs])
            for node in preMap[crs]:
                if not dfs(node):
                    return False
            visiting.remove(preMap[crs])
            '''the line below this is really important, it essentially guarantees that a specific node's path is only traversed once'''
            preMap[crs] = [] 
            return True


        for crs in range(len(prerequisites)):
            if not dfs(crs):
                return False

        return True
        
            
