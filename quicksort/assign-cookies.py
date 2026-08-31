class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int: #定义一个函数，接收两个整数列表作为输入，并以一个整数作为输出
        g.sort() #定义函数记得要有缩进块
        s.sort()
        chidren_num = len(g)
        cookie_num = len(s)
        chidren = 0
        cookie = 0

        while chidren < chidren_num and cookie < cookie_num:
            if g[chidren] <= s[cookie]:
                chidren = chidren + 1
                cookie = cookie + 1
            else:
                cookie = cookie + 1
            
        return chidren