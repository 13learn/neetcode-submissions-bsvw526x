class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        ans = nums[0]

        for i in range(len(nums)):

            cur = nums[i]

            for j in range(i + 1, len(nums)):

                ans = max(ans, cur)

                cur += nums[j]
                
            ans = max(ans, cur)
        

        return ans
        