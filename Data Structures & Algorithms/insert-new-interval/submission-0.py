class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # no merging needed for remaining intervals
            if newInterval[1] < intervals[i][0]: 
                res.append(newInterval)
                return res + intervals[i:]
            # no merging needed for this interval
            elif newInterval[0] > intervals[i][1]: 
                res.append(intervals[i])
            
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])]
        # appending for the case where new interval is right to the last interval
        res.append(newInterval)

        return res


        