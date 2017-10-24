# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.abs = 0
        def sum_node(root):
            if not root:
                return 0
            left, right = sum_node(root.left), sum_node(root.right)
            self.abs += abs(left - right)
            return left + right + root.val
        sum_node(root)
        return self.abs
