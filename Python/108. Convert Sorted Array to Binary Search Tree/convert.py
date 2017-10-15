# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        l = len(nums)//2
        root = TreeNode(nums[l])
        root.left = self.sortedArrayToBST(nums[:l])
        root.right = self.sortedArrayToBST(nums[l+1:])
        return root
