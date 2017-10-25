class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(' ')
        for i in range(len(words) - 1, -1, -1):
            words[i].replace(' ', '')
            if words[i] != '':
                return len(words[i])
        return 0
