class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}

        for num in nums:
            freq_count[num] = 1 + freq_count.get(num, 0)
        
        sorted_list = []

        for num, freq in freq_count.items():
            sorted_list.append([freq, num])
        
        sorted_list.sort()

        res = []

        while len(res) < k:
            res.append(sorted_list.pop()[1])

        return res        