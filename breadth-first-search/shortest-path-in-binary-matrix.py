class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # Check start and end
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # 8 directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # BFS: (row, col, path_length)
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1  # Mark as visited

        while queue:
            r, c, dist = queue.popleft()

            # Reach destination
            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, dist + 1))
                    grid[nr][nc] = 1  # Mark as visited

        return -1
        