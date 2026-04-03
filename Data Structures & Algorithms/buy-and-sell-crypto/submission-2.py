class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # min_p = prices[0]
        # max_p = 0

        # for p in prices:
        #     max_p = max(max_p, p - min_p)
        #     min_p = min(min_p, p)
        
        # return max_p
        l, r = 0, 1
        max_p = 0

        while r < len(prices):

            if prices[r] > prices[l]:
                max_p = max(max_p , prices[r] - prices[l])
            
            else:
                l = r
            r += 1

        return max_p        