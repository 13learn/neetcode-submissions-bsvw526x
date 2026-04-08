class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        prev_seen_prefix_sum = defaultdict(int)
        prev_seen_prefix_sum[0] = 1

        prefix_sum = 0

        for num in nums:

            prefix_sum += num

            # look for prefix_sum - k in pervious iterations
            count += prev_seen_prefix_sum.get(prefix_sum - k, 0)


            prev_seen_prefix_sum[prefix_sum] += 1
        
        return count

        