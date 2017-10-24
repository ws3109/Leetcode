class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        num = x
        while num * num > x:
            num = (num + x/num) / 2
        return num
