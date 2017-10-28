# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        num_left = self.num_of_nodes(root.left)
        if k <= num_left:
            return self.kthSmallest(root.left, k)
        elif k == num_left + 1:
            return root.val
        elif root.right:
            return self.kthSmallest(root.right, k - num_left - 1)
    
    def num_of_nodes(self, root):
        if not root:
            return 0
        return self.num_of_nodes(root.left) + self.num_of_nodes(root.right) + 1
        
        
