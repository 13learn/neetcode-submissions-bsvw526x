class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums.sort()

        ans = 1
        cur_streak = 1
        i = 0
        while i < len(nums) - 1:

            if nums[i] == nums[i + 1]:
                i += 1
                continue
            if nums[i] + 1 == nums[i + 1]:
                cur_streak += 1
            else:
                ans = max(ans, cur_streak)
                cur_streak = 1
            i += 1
        ans = max(ans, cur_streak)
        
        return ans




        