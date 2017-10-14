# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        l = {}
        self.traverseByLevel(root, l, 0)
        # Be careful about the division. 
        result = [sum(l[x])*1.0/len(l[x]) for x in l]
        return result
        
    def traverseByLevel(self, root, l, depth):
        if not root:
            return
        if depth not in l:
            l[depth] = []
        l[depth].append(root.val)
        self.traverseByLevel(root.left, l, depth + 1)
        self.traverseByLevel(root.right, l, depth + 1)
        
