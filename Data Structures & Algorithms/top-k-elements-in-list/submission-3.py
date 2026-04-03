class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        
        freq_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))

        return list(freq_dict.keys())[:k]
        