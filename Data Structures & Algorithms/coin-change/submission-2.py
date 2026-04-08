class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        temp = amount + 1
        mem = [[amount + 1] * (amount + 1) for _ in range(len(coins) + 1)] 

        for i in range(len(mem)):
            # amount = 0 
            mem[i][0] = 0
        
        for j in range(len(mem[0])):
            mem[0][j] = float('inf')
        # if no coins left and no sum left
        mem[0][0] = 0
        def check(n, amount):
            if mem[n][amount] != temp:
                return mem[n][amount]

            if amount == 0:
                return 0
            
            if n == 0:
                return float('inf')
            
            if coins[n - 1] > amount:
                mem[n][amount] = check(n - 1, amount)
                return mem[n][amount]
            
            else:
                mem[n][amount] = min(1 + check(n, amount - coins[n - 1]),
                check(n - 1, amount))
                return mem[n][amount]
        result = check(len(coins), amount)
        return result if result != float('inf') else -1

            

            

        