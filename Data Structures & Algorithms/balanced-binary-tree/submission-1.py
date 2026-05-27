# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            lVal, rVal = dfs(root.left), dfs(root.right)
            balanced = lVal[0] and rVal[0] and abs(lVal[1] - rVal[1]) <= 1
            return [balanced, 1 + max(lVal[1], rVal[1])]
        return dfs(root)[0]