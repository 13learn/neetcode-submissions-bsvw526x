class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])  
        current_interval = intervals[0]
        res = []
        for i in range(1, len(intervals)):

            if current_interval[1] < intervals[i][0]:
                res.append(current_interval)
                current_interval = intervals[i]
            
            else:
                current_interval = [min(current_interval[0],
                intervals[i][0]), max(current_interval[1], intervals[i][1])]
        res.append(current_interval)
        return res
        