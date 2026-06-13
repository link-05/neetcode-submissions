# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.sameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if not (root.val == subRoot.val):
            return False
        purity = True
        if root.left and subRoot.left:
            purity = purity and self.sameTree(root.left, subRoot.left)
        elif not(root.left == subRoot.left): 
            return False
        if root.right and subRoot.right:
            purity = purity and self.sameTree(root.right, subRoot.right)
        elif not(root.right == subRoot.right): 
            return False
        return purity