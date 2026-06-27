# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        out = 0

        def dfs(node):
            nonlocal out
            if node == None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            print(left,right)
            out = max(out, left + right)
            return 1 + max(left,right)

        dfs(root)
        return out

'''

When we calculate the diameter, we want to A. Update the height of the tree so that we can compute diameters from higher nodes
B: update the global variable so that we can keep track of the greatest diameter that we have seen so far   

'''
