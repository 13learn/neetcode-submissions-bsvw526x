class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        l = 0 # day for buy
        for r in range(1, len(prices)):
            current_balance = prices[r] - prices[l]

            if current_balance < 0:
                l = r
            best_profit = max(best_profit, current_balance)
        return best_profit
        