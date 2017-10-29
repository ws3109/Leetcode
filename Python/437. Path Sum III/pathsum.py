# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum_orig):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.cnt = 0
        def dfs(root, val):
            if not root:
                return 0 
            res = (val == root.val)
            res += dfs(root.left, val - root.val)
            res += dfs(root.right, val - root.val)
            return res
        if not root:
            return 0
        ans = dfs(root, sum_orig)
        ans += self.pathSum(root.left, sum_orig)
        ans += self.pathSum(root.right, sum_orig)
        return ans
        
