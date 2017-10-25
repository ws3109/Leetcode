# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        self.flatten(root.left)
        self.flatten(root.right)
        right = root.right
        root.right = root.left
        root.left = None
        while root and root.right:
            root = root.right
        root.right = right
        
        
        
