import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [0]*n
        count = 0
        cost = 0
        heap = [(0,0)]
        while count < n:
            cost_add , a = heapq.heappop(heap)
            if visited[a]:
                continue
            else:
                count += 1
                cost += cost_add
                visited[a] = 1
                for i in range(n):
                    if visited[i] == 0:
                        distance = abs(points[a][0] - points[i][0]) + abs(points[a][1] - points[i][1])
                        heapq.heappush(heap,(distance, i))
                    else:
                        continue
        return cost


        