class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0, 1]
        n = 2
        while n <= num:
            temp = ans[n//2: n]
            ans.extend(temp + [x+1 for x in temp])
            n += n
        return ans[0:num+1]
            
