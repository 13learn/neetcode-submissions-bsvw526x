class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            
            #start of a new sequence
            if num - 1 not in nums_set:
                cur_seq_len = 1
                while num + cur_seq_len in nums_set:
                    cur_seq_len += 1
                ans = max(ans, cur_seq_len)
        return ans



                


        