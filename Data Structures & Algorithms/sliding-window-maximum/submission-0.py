class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        ans = []
        for i in range(len(nums)):

            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            deq.append(i)

            # remove out of bound index
            if deq[0] == i - k: 
                deq.popleft()
            
            if i >= k - 1:
                ans.append(nums[deq[0]])
        
        return ans

            
        