# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        inorder_result = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                break
            root = stack.pop()
            inorder_result.append(root.val)
            root = root.right
        return inorder_result
        
        
        
