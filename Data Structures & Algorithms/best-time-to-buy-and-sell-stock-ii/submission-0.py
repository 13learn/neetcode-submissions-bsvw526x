class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l, r = 0, 1

        for r in range(1, len(prices)):

            if prices[r] < prices[r - 1]:
                # print(r - 1, l)
                max_p += prices[r - 1] - prices[l] # sell on previous day
                l = r # option to buy at r

        # sale on last day case 
        # print("outside", r, l)
        max_p += prices[r] - prices[l]
    
        return max_p
        