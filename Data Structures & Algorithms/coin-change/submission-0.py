class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        minways = [amount + 1] * (amount + 1)

        minways[0] = 0

        for x in range(1, amount + 1):
            for coin in coins:

                if x - coin >= 0:
                    minways[x] = min(minways[x], minways[x - coin] + 1)
        
        if minways[amount] == amount + 1:
            return -1
        
        return minways[amount]



        