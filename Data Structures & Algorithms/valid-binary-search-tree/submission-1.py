# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minThres, maxThres):
            if not root:
                return True
            if root.val > minThres and root.val < maxThres:
                return dfs(root.left, minThres, root.val) and dfs(root.right, root.val, maxThres)
            else:
                return False
        return dfs(root, float('-inf'), float('inf'))
