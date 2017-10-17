class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) in range(1, 3):
            return max(nums)
        min_value = float('-inf')
        first, second, third = min_value, min_value, min_value
        for x in nums:
            if x > first:
                first, second, third = x, first, second
            elif x > second and x < first:
                second, third = x, second
            elif x > third and x < second:
                third = x
        if third == min_value or second == min_value:
            return first
        return third
        
