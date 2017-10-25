class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            triangle.append([1 for _ in range(i+1)])
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle[:numRows]
                
        
