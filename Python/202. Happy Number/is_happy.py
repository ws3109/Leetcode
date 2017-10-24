class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exist = {}
        while True:
            if n == 1:
                return True
            if n in exist:
                return False
            exist[n] = True
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n //= 10
            n = temp
