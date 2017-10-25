# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.max_val = {}
        def dfs(root, depth):
            if not root:
                return
            if depth not in self.max_val:
                self.max_val[depth] = root.val
            else:
                self.max_val[depth] = max(self.max_val[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return self.max_val.values()
        
        
