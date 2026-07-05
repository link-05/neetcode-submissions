# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, value: int) -> int:
            if root.val >= value:
                sumGood = 1
            else:
                sumGood = 0
            maxVal = max(root.val, value)
            if root.left:
                sumGood += dfs(root.left, maxVal)
            if root.right:
                sumGood += dfs(root.right, maxVal)
            return sumGood
        if root:
            return dfs(root, root.val)
        else:
            return 0