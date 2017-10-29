class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False
        m, n = len(board), len(board[0])
        visited = None
        def dfs(i, j, k):
            if i < 0 or i == m or j < 0 or j == n or (i, j) in visited or word[k] != board[i][j]:
                return False
            if k == len(word) - 1:
                return True
            else:
                visited[(i, j)] = True
                result = dfs(i-1, j, k) or dfs(i+1, j, k) or dfs(i, j - 1, k) or dfs(i,j + 1, k)
                visited.pop((i, j))
                return result
        for i in range(m):
            for j in range(n):
                visited = {}
                if dfs(i, j, 0):
                    return True
        return False
