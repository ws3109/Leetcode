class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        result = ""
        for i in range(len(s)//k + len(s) % k):
            bound = min((i+1)*k, len(s))
            result = result + s[i*k: bound][::-1] if i % 2 == 0 else result + s[i*k: bound]
        return result
        
