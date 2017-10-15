class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        cur, ans = 1, 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cur = cur + 1
            else:
                cur, ans = 1, max(cur, ans)
        return max(cur, ans)
                
                
