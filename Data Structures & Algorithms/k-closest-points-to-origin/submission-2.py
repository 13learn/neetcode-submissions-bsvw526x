
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        import heapq
        closest_k = []
        for x, y in points:
            squared_distance = x**2 + y**2
            heapq.heappush(closest_k, [-squared_distance, x, y])

            if len(closest_k) > k:
                heapq.heappop(closest_k)
            
        ans = []
        while closest_k:
            dist, x, y = closest_k.pop()
            ans.append([x, y])
        
        return ans



        
        