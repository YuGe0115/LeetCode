class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        #BFS
        queue = deque()
        queue.append(source)



        adjacent = [[] for _ in range(n)]
        for a,b in edges:
            adjacent[a].append(b)
            adjacent[b].append(a)

        visited = [0 for _ in range(n)]
        visited[source] = 1

        while queue:
            point = queue.popleft()
            if destination in adjacent[point]:
                return True
            elif destination == point:
                return True
            else:
                for neighbor in adjacent[point]:
                    if visited[neighbor] == 0:
                        queue.append(neighbor)
                        visited[neighbor] = 1
        return False


        