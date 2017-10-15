# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def bfs(root, l, depth):
            if not root: return
            if depth not in l:
                l[depth] = []
            l[depth].append(root.val)
            bfs(root.left, l, depth + 1)
            bfs(root.right, l, depth + 1)
        l = {}
        bfs(root, l, 0)
        return list(l.values())[::-1]
        
