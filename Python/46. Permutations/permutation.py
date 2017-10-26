class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.n = len(nums)
        results = []
        def dfs(nums, index, results):
            if index == self.n:
                results.append(nums[:])
                return
            for i in range(index, self.n):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(nums, index + 1, results)
                nums[index], nums[i] = nums[i], nums[index]
        dfs(nums, 0, results)
        return results
