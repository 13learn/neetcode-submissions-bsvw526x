class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        num_freq = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]
        ans = []
        for num in nums:
            num_freq[num] += 1
        for key, value in num_freq.items():
            buckets[value].append(key)
        count = 0
        for i, values in enumerate(buckets[::-1]):
            if not value:
                continue
            for val in values:
                if count == k:
                    return ans
                ans.append(val)
                count += 1
        return ans

        

        