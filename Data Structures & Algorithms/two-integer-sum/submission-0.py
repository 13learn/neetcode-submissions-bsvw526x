class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {n: i for i, n in enumerate(nums)}

        for i in range(len(nums)):
            if (target - nums[i]) in index_map and index_map[target - nums[i]] != i:
                return [i, index_map[target - nums[i]]]
        