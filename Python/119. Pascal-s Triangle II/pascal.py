class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rows = [[1 for _ in range(rowIndex + 1)] for _ in range(2)]
        for i in range(1, rowIndex + 1):
            index = i % 2
            for j in range(1, i):
                rows[index][j] = rows[index^1][j-1] + rows[index^1][j]
        return rows[rowIndex % 2]
        
