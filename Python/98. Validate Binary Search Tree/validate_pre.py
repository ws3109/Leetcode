# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre = float('-inf')
        return self.valid(root)
    
    def valid(self, root):
        if not root:
            return True
        if not self.valid(root.left) or self.pre >= root.val:
            return False
        self.pre = root.val
        return self.valid(root.right)
