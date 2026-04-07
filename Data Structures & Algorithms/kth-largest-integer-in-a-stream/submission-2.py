import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # max heap
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        rem_ele = []
        for i in range(self.k):
            rem_ele.append(-heapq.heappop(self.nums))
        ans = rem_ele[-1] # kth largest
        for num in rem_ele:
            heapq.heappush(self.nums, - num)
        return ans



        

        
