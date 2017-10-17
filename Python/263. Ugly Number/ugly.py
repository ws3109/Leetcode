class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        factors = [2, 3, 5]
        for f in factors:
            while num % f == 0:
                num /= f
        return num == 1
        
