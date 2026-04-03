class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]

        cur = 0

        for i in range(len(nums)):

            cur += nums[i]

            
            
            ans = max(ans, cur)
            if cur < 0:
                cur = 0
        
        return ans

        
        