class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_prod = [1 for _ in range(n)]
        for i in range(1, n):
            left_prod[i] = nums[i-1] * left_prod[i-1]
        right_prod = 1
        for i in range(n-1, -1, -1):
            left_prod[i] *= right_prod
            right_prod *= nums[i]
        return left_prod
        
        
