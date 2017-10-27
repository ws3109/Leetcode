class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, filter(lambda x : x & xor & -xor, nums))
        return [ans, ans ^ xor]
