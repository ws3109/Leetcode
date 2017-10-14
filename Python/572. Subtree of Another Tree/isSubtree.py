# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.same(s, t):
            return True
        return s.left != None and self.isSubtree(s.left, t) or s.right != None and self.isSubtree(s.right, t)
    
    def same(self, s, t):
        if not s and not t:
            return True
        elif not s or not t or s.val != t.val:
            return False
        else:
            return self.same(s.left, t.left) and self.same(s.right, t.right) 
