# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.pre = float('-inf')
        self.count = 0
        self.max = 0
        self.maxList = []
        def traverse(root):
            if not root:
                return 
            traverse(root.left)
            if root.val > self.pre:
                self.count = 1
                self.pre = root.val
            else:
                self.count += 1
            
            if self.count > self.max:
                self.max, self.maxList = self.count, [root.val]
            elif self.count == self.max:
                self.maxList.append(root.val)
            traverse(root.right)
        traverse(root)
        return self.maxList
            
                
        
