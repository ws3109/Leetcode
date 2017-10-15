class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = float('inf'), 0
        for x in nums:
            if x == candidate:
                count += 1
            else:
                count -= 1
                if count < 0:
                    candidate, count = x, 1
        return candidate
            
        
