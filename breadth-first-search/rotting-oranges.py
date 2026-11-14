class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # BFS from different starting nodes
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        times = 0

        while queue:
            changed = False

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for r_add, c_add in directions:
                    r_new = r + r_add
                    c_new = c + c_add

                    if (0 <= r_new < len(grid)
                        and 0 <= c_new < len(grid[0])
                        and grid[r_new][c_new] == 1):

                        grid[r_new][c_new] = 2
                        queue.append((r_new, c_new))
                        changed = True

            if changed:
                times += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return times

