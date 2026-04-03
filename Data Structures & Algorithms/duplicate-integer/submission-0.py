class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return True
        return False
        