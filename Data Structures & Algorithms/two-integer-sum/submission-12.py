class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = 0
        for i, n in enumerate(nums):
            if target - n in nums[i + 1:]: # O(n) operation 
                match = n
                break
        s_idx = nums.index(match)
        e_idx = nums.index(target - match, s_idx + 1)
        return sorted([s_idx, e_idx])

        



        