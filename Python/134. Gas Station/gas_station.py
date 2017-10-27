class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        start = 0
        for x in range(len(cost)):
            total += gas[x] - cost[x]
            if total < 0:
                start, total = x + 1, 0
        return start if sum(gas) >= sum(cost) else -1
