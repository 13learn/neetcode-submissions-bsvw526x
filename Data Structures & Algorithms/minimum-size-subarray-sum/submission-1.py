class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, r = 0, 0
        n = len(nums)
        ans = n + 1
        cur_sum = 0
        for r in range(n):
            cur_sum += nums[r]
            while cur_sum >= target and l <= r:
                ans = min(ans, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        return ans if ans != n + 1 else 0
            


        