class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans, neg, x = 0, x < 0, abs(x)
        while x > 0:
            ans = ans * 10 + x % 10
            x /= 10
        return 0 if ans > 0x7FFFFFFF else -ans if neg else ans
            
        
        
        
