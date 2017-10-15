class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.l = []
        def dfs(nums, index, cur):
            if index == len(nums):
                self.l.append(list(cur))
                return
            dfs(nums, index + 1, cur + [nums[index]])
            dfs(nums, index + 1, cur)
        if len(nums) > 0:
            dfs(nums, 0, [])
        return self.l
