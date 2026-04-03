class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        max_len = 1
        uni_nums = set(nums)

        for i in range(len(nums)):

            cur_max = 1
            cur_ele = nums[i]

            while cur_ele + 1 in uni_nums and cur_max <= len(nums):
                cur_ele += 1
                cur_max += 1
                max_len = max(max_len, cur_max)

        
        
        return max_len




        