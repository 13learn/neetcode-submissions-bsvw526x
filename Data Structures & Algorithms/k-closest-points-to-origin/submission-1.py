
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [ ((x**2 + y**2)**0.5, (x, y)) for x, y in points]

        import heapq

        heapq.heapify(distances)

        ans = []

        while len(ans) < k:
            close, points = heapq.heappop(distances)
            ans.append(list(points))
        
        return ans

        
        