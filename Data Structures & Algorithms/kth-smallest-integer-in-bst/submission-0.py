# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # This is inorder traversal 
        # Count from inorder
        # Track count and save result
        self.count = 0
        self.retVal = None
        def inorder(root, k):
            if root.left:
                inorder(root.left, k)
            self.count += 1
            if self.count == k:
                self.retVal = root.val
            if root.right:
                inorder(root.right, k)
        if root:
            inorder(root, k)
            return self.retVal
        else:
            return -1
        