# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.symmetric(root.left, root.right)
    
    def symmetric(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None or left.val != right.val:
            return False
        else:
            return self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)
