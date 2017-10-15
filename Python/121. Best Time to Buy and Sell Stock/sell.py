class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        dif = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        ans, cur = float('-inf'), 0 
        for x in dif:
            cur = cur + x
            ans = max(ans, cur)
            cur = cur if cur >= 0 else 0
        return max(ans, 0)
        
