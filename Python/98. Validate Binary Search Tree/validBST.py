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
        if not root or (not root.left and not root.right):
            return True
        left_valid = self.isValidBST(root.left)
        right_valid = self.isValidBST(root.right)
        if not left_valid or not right_valid:
            return False
        left_max, right_min = root.left, root.right
        while left_max and left_max.right:
            left_max = left_max.right
        while right_min and right_min.left:
            right_min = right_min.left
        return (not left_max or root.val > left_max.val) and (not right_min or root.val < right_min.val)
        
