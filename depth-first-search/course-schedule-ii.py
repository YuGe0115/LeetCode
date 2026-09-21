class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # topological ordering
        # BFS: record the degree_in of all vertice. If vertex A has degree_in of 0: pick it and delete it from the graph + decrease all its neibour's degree_in by 1

        # First, make the graph
        # a list to record the neibours
        # a list to record the indegrees
        neibours = [[] for _ in range(numCourses)]
        indegree = [0]* numCourses

        for course, pre in prerequisites:
            neibours[pre].append(course)
            indegree[course] += 1
        
        result = []
        # BFS Start
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            vertex = queue.popleft()
            for i in neibours[vertex]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            result.append(vertex)
        
        if len(result) == numCourses:
            return result
        else:
            return []