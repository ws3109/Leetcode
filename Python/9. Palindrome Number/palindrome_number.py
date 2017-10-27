class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        l = int(math.log(x, 10))
        while x > 0:
            low = x % 10
            high = x // 10 ** l
            if low != high:
                return False
            x = (x % 10 ** l)//10
            l -= 2
        return True
        
        
        
