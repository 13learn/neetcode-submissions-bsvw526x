class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        
        intervals = sorted(intervals, key=lambda x:x[0])
        current = intervals[0]
        i = 1

        while i < len(intervals):

            while i < len(intervals) and intervals[i][0] <= current[1]:
                current = [min(intervals[i][0], current[0]),
                max(intervals[i][1], current[1])]
                i += 1
                
            ans.append(current)
            
            if i < len(intervals):
                current = intervals[i]
                i += 1
        
        if not ans or ans[-1] != current:
            ans.append(current)
        
        return ans