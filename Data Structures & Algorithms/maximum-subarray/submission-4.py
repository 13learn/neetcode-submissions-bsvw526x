class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = nums[0]
        cur = nums[0]

        for i in range(1, len(nums)):

            if cur + nums[i] < 0:
                cur = 0
                ans = max(ans, nums[i])
                continue
            cur += nums[i]
            ans = max(ans, cur)
        
        return ans
        