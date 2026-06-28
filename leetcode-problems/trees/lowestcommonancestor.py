# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

The trick is that a node is the LCA if p and q split off that node, 
eg, something like the root node val = 5, when the p.val is 3 and q.val is 6,
then after that split, we know that the root node is the LCA. If not,
we recursively solve until we find a node that is equal to p and q. If we 
find one of these nodes, then that node is the LCA. 


'''
class Solution:

def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None:
            return 0
        out = root

        #THIS IS A BST!!!
    def search(root,p,q):
    nonlocal out
    print(p.val,q.val,root.val)
        if p.val < root.val and q.val > root.val:
            out = root
            return root.val
        elif p.val > root.val and q.val < root.val:
            out = root
            return root.val

        if p.val > root.val and q.val > root.val:
            search(root.right,p,q)

        if p.val < root.val and q.val < root.val:
            search(root.left,p,q)

        if p.val == root.val:
            out = p
            return p.val
        elif q.val == root.val:
            out = q
            return q.val

    self.search(root,p,q)
    return out 
