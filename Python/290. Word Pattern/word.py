class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_to_word = {}
        word_to_str = {}
        words = string.split(' ')
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if words[i] not in word_to_str and pattern[i] not in str_to_word:
                word_to_str[words[i]] = pattern[i]
                str_to_word[pattern[i]] = words[i]
            elif words[i] in word_to_str and pattern[i] in str_to_word and word_to_str[words[i]] == pattern[i]\
                 and str_to_word[pattern[i]] == words[i]:
                    continue
            else:
                return False
        return True
        
