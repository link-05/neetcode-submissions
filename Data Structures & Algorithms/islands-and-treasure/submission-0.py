class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        visited = set()
        # Find all treasure
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If grid is not traversable
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i, j))
        dist = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q: 
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == -1 or (row, col) in visited):
                        continue
                    q.append((row, col))
                    visited.add((row, col))
            dist += 1