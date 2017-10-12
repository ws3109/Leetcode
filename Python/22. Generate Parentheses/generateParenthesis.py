class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, n, '', result)
        return result
    
    def generate(self, ln, rn, cur, result):
        if rn < ln:
            return
        if ln == 0 and rn == 0:
            result.append(cur)
        if ln > 0:
            self.generate(ln-1, rn, cur + '(', result)
        if rn > 0:
            self.generate(ln, rn-1, cur + ")", result)
        
