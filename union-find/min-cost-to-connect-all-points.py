import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited =[False]*n
        heap = [(0,0)] #(distance, vertex)
        count = 0
        total_cost = 0

        while count < n :
            cost, u =heapq.heappop(heap)
            if visited[u]:
                continue
            
            visited[u] = True
            total_cost = total_cost + cost
            count += 1

            for v in range(n):
                if not visited[v]:
                    distance = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (distance, v))
    
        return total_cost



        