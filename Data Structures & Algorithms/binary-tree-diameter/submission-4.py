# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.val = 0
        def dfs(node):
            lMax = 0
            rMax = 0
            if node == None:
                return 0
            if node.left:
                lMax = dfs(node.left)
            if node.right:
                rMax = dfs(node.right)
            self.val = max(self.val, lMax + rMax)
            return 1 + max(lMax, rMax)
        dfs(root)
        return self.val

        