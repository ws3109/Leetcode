class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        stot, ttos = {}, {}
        for i in range(len(s)):
            if s[i] not in stot and t[i] not in ttos:
                stot[s[i]], ttos[t[i]] = t[i], s[i]
            elif s[i] in stot and t[i] in ttos and stot[s[i]] == t[i] and ttos[t[i]] == s[i]:
                continue
            else:
                return False
        return True
