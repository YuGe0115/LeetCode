class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
    
        dic_r = {}
        for i in grid:
            row = tuple(i)
            dic_r[row] = dic_r.get(row,0) + 1
    
        dic_c = {}
        for i in range(len(grid[0])):
            col = tuple(grid[j][i] for j in range(len(grid)))
            dic_c[col] = dic_c.get(col,0) + 1
        

        result = 0
        for key in dic_c:
            if key in dic_r:
                result += dic_c[key] * dic_r[key]
        
        return result
