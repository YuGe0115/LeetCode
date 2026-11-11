class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # BFS: FIFO
        queue = deque()
        queue.append((sr,sc))

        n = len(image)
        m = len(image[0])

        origin_color = image[sr][sc]

        if image[sr][sc] == color:
            return image

        image[sr][sc] = color

        while queue:
            current_r, current_c = queue.popleft()
            for r_add, c_add in [(-1,0),(0,1),(0,-1),(1,0)]:
                if 0<= current_r + r_add <= n-1 and  0<= current_c + c_add <= m-1 and image[current_r + r_add][current_c + c_add] == origin_color:
                    image[current_r + r_add][current_c + c_add] = color
                    queue.append((current_r + r_add,current_c + c_add))
        
        return image

