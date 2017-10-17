class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        x, total = 2, 1
        while x * x <= num:
            if num % x == 0:
                total += x
                if x * x != num:
                    total += num / x
            x += 1
        return total == num
        
