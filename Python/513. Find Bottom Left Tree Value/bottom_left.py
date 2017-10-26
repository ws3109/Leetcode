# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = -1
        self.left_most_val = 0
        def dfs(root, depth):
            if not root:
                return
            if depth > self.max_depth:
                self.max_depth = depth
                self.left_most_val = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return self.left_most_val
