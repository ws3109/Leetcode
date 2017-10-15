class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "": 
            return True
        result = []
        for c in s:
            if c.isalpha():
                result.append(c.lower())
            elif c.isnumeric():
                result.append(c)
        return result == result[::-1]
        
