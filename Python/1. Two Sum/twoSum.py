class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted([(nums[i], i) for i in range(len(nums))])
        l, r = 0, len(nums) - 1
        while l < r:
            lx, li = nums[l]
            rx, ri = nums[r]
            if lx + rx == target:
                return sorted([li, ri])
            elif lx + rx < target:
                l += 1
            else:
                r -= 1
            
            
            
        
