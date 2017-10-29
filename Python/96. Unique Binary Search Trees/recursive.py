class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = [[0 for _ in range(n+1)] for _ in range(n+1)]
        def count(l, r):
            if r <= l:
                return 1
            if c[l][r] > 0:
                return c[l][r]
            for i in range(l, r+1):
                c[l][r] += count(l, i - 1) * count(i+1, r) 
            return c[l][r]
        return count(1, n)
        
