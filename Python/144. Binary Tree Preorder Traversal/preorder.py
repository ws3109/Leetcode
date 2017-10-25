# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder_result = []
        stack = []
        while root or stack:
            if root:
                preorder_result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right 
        return preorder_result
    
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder_result = []
        stack = []
        while root or stack:
            while root:
                preorder_result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right 
        return preorder_result
                
