# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if root:
            self.search(root, '', result)
        return result
    
    def search(self, root, path, result):
        path = path + str(root.val)
        if not root.left and not root.right:
            result.append(path)
            return
        if root.left:
            self.search(root.left, path + '->', result)
        if root.right:
            self.search(root.right, path + '->', result)
