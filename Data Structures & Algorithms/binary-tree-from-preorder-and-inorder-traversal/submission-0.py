# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # To rebuild a tree using preorder and inorder
        # inorder is left root right
        # preorder is root left right            
        # If either list is empty
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = -1
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                mid = i
                break
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        