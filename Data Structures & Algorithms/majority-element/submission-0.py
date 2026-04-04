class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        need_count = len(nums) // 2

        for num in nums:
            count[num] += 1
            if count[num] > need_count:
                return num
        
        return 0

        
        