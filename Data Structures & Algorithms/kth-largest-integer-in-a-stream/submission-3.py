import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # max heap
        self.array = []
        self.k = k
        for num in nums:
            _ = self.add(num)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.array, val)

        if len(self.array) > self.k:
            heapq.heappop(self.array)
        
        return self.array[0]

        



        

        
