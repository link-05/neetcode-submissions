class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.seen = set()
        def dfs(i, j, target):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i,j) in self.seen:
                return False
            if board[i][j] == target:
                return True
            if board[i][j] != target[0]:
                return False
            self.seen.add((i,j))
            res = (dfs(i+1, j, target[1:]) or dfs(i-1,j, target[1:]) or dfs(i, j+1, target[1:]) or dfs(i, j-1, target[1:]))
            # Backtrack
            self.seen.remove((i, j))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.seen = set()
                if dfs(i, j, word):
                    return True
        return False