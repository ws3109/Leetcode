class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        n = len(nums)
        k = k % n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
