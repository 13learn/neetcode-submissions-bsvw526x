class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict

        freq = defaultdict(int)

        for n in nums:
            if freq[n] > 0:
                return True
            freq[n] += 1

        return False
        
        