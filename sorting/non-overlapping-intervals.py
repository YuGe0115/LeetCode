class Solution:
    #总体想法：先把区间排序，然后再按顺序逐个筛选，尽量只保留占的位置最小的
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1]) #lamda形式为“参数：表达式”，不可复用但是简洁
        m = 0
        end = intervals[0][1]
        for i in range(0,len(intervals)-1):
            if intervals[i+1][0] < end:
                m += 1
            else:
                end = intervals[i+1][1]
        return m

        