# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0
        def find_max_len(root):
            if not root:
                return 0
            left_len, right_len = find_max_len(root.left), find_max_len(root.right)
            l_same, r_same = False, False
            if not root.left or root.val != root.left.val:
                left_len = 0
            elif root.val == root.left.val:
                l_same = True
                left_len += 1
            if not root.right or root.val != root.right.val:
                right_len = 0
            elif root.val == root.right.val:
                r_same = True
                right_len += 1
            if l_same and r_same:
                self.max_len = max(self.max_len, left_len + right_len)
            else:
                self.max_len = max(self.max_len, max(left_len, right_len))
            return max(left_len, right_len)
        find_max_len(root)
        return self.max_len
    
