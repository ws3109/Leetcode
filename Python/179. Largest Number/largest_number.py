class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
            return int(b + a) - int(a + b)
        nums = sorted([str(x) for x in nums],cmp = compare)
        ans = ''.join(nums).lstrip('0')

        return ans or '0'
