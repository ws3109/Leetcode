# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(l, r):
            if l > r:
                return [None]
            elif l == r:
                return [TreeNode(l)]
            else:
                results = []
                for i in range(l, r + 1):
                    left_nodes = generate(l, i-1)
                    right_nodes = generate(i+1, r)
                    for left_node in left_nodes:
                        for right_node in right_nodes:
                            root = TreeNode(i)
                            root.left = left_node
                            root.right = right_node
                            results.append(root)
                return results
        if n == 0:
            return []
        return generate(1, n)

        
