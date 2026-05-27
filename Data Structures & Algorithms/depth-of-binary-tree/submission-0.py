# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        lMax = 1
        rMax = 1
        if root == None:
            return 0
        if root.left:
            lMax = self.maxDepth(root.left) + 1
        if root.right:
            rMax = self.maxDepth(root.right) + 1
        return lMax > rMax and lMax or rMax