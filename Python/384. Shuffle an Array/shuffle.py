import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.init_nums = nums[:]
        self.cur_nums = nums[:]
        self.n = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.cur_nums = self.init_nums[:]
        return self.cur_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(self.n):
            index = random.randint(i, self.n - 1)
            self.cur_nums[i], self.cur_nums[index] = self.cur_nums[index], self.cur_nums[i]
        return self.cur_nums 


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
