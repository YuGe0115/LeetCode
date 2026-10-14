class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # imagine it is a graph, and to find islands means finding connected components
        # DFS or BFS
        
        # DFS: stack
        # BFS: FIFO, queue

        n = len(grid)
        m = len(grid[0])

        stack = []
        count = 0

        visited = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    visited[i][j] = 1
                    stack.append((i,j))

                    while stack:
                        i_stack, j_stack = stack.pop()
                        directions = [(1,0),(-1,0),(0,1),(0,-1)]
                        for x_add, y_add in directions:
                            n_new = i_stack + x_add
                            m_new = j_stack + y_add
                            if not((0 <= n_new <= n-1) and (0 <= m_new <= m-1)):
                                continue
                            if grid[n_new][m_new] == "1" and visited[n_new][m_new] == 0:
                                visited[n_new][m_new] = 1
                                stack.append((n_new,m_new))
    
        return count

                        





        