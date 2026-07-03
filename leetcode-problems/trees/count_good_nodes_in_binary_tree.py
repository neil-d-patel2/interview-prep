class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root == None:
            return 0

        def dfs(root, maxVal):
            if root == None:
                return 0

            out = 1 if root.val >= maxVal else 0
            maxVal = max(root.val, maxVal)
            out += dfs(root.left, maxVal)
            out += dfs(root.right, maxVal)
            return out

        return dfs(root, root.val)

