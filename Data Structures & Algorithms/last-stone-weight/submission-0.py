class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapq.heapify(stones) # 0(n)

        while len(stones) > 1:

            max1 = -heapq.heappop(stones)
            max2 = -heapq.heappop(stones)

            if max1 != max2:
                print(max1, max2)
                heapq.heappush(stones, max2 - max1)
        
        return -stones[0] if stones else 0




        