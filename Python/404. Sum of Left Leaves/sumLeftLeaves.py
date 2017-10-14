# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, isLeft):
            if not root: return 0
            if not root.left and not root.right and isLeft:
                return root.val
            return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)
        
