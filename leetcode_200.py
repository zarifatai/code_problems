from typing import List
from collections import deque


class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        return res

    def num_islands_2(self, grid: List[List[str]]) -> int:
        self.grid = grid
        if not self.grid:
            return 0

        count = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == "1":
                    count += 1
                    self.bfs(row, col)
        return count

    def bfs(self, row, col):
        if (
            row < 0
            or row >= len(self.grid)
            or col < 0
            or col >= len(self.grid[0])
            or self.grid[row][col] != "1"
        ):
            return

        self.grid[row][col] = "2"
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for dr, dc in directions:
            self.bfs(row + dr, col + dc)
