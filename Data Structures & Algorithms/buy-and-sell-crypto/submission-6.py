class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l, r = 0, 1

        while r < len(prices):

            while prices[r] < prices[l] and l < r:
                l += 1
            
            ans = max(ans, prices[r] - prices[l])

            r += 1
        
        return ans
        