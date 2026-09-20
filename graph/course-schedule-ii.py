class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # topological ordering
        # BFS

        # First, create the graph
        graph = [[] for _ in range(numCourses)] #out
        indegree = [0] * numCourses
        for pre, course in prerequisites:
            graph[course].append(pre)
            indegree[pre] += 1
            
        # BFS: FIFO
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            selected = queue.popleft()
            result.append(selected)
            for i in graph[selected]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        if len(result) == numCourses:
            return result
        else:
            return[]
