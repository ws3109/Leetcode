class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        'MMMCM = 3900 = 3000 + 100 + 1000 - 200'
        l = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for i in range(len(s)):
            num += l[s[i]]
            if i > 0 and l[s[i-1]] < l[s[i]]:
                num -= 2*l[s[i-1]]
        return num
        
        
