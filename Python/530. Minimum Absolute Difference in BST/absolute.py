# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.last = -0x80000000
        self.ans = 0x7FFFFFFF
        def inOrder(root):
            if not root: return 
            inOrder(root.left)
            self.ans = min(self.ans, root.val - self.last)
            self.last = root.val
            inOrder(root.right)
        inOrder(root)
        return self.ans
            
        
