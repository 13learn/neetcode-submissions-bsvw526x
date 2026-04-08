class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        ans = n + 1

        for i in range(n):
            current = 0
            for j in range(i, n):
                current += nums[j]

                if current >= target:
                    ans = min(ans, j - i + 1)
                    break
        
        return ans if ans != n + 1 else 0
        