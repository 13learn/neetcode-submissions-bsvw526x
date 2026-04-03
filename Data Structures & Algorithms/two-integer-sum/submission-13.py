class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        first_idx , second_idx = 0, 0
        for i in range(len(nums)):
            if target - nums[i] not in seen:
                seen.add(nums[i])
                continue
            second_idx = i   
            break
        
        for j in range(len(nums)):
            if target - nums[second_idx] == nums[j]:
                first_idx = j
                break


        return [first_idx, second_idx]
        