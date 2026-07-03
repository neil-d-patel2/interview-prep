class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        out = [root.val]

        def dfs(root):
            nonlocal out
            if root == None:
                return

            dfs(root.left)
            out.append(root.val)
            dfs(root.right)

        for i in range (0,len(out)-1):
            if out[i] > out[i+1]:
                return False

        return True
