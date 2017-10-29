class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        covered = 0 
        for i in range(len(nums) - 1):
            if covered < i:
                return False
            covered = max(covered, i + nums[i])
        return len(nums) - 1 <= covered
        
        
