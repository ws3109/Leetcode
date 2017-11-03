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
        return self.valid(root, float('-inf'), float('inf'))
    def valid(self, root, MIN, MAX):
        if not root: return True
        if root.val <= MIN or root.val >= MAX:
            return False
        return self.valid(root.left, MIN, root.val) and self.valid(root.right, root.val, MAX)
