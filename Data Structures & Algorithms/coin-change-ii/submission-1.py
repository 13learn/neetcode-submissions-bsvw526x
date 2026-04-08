class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        mem = [ [-1] * (len(coins) + 1) for _ in range(amount + 1)]

        for i in range(len(mem[0])):
            mem[0][i] = 1 


        def check(amount, n):

            if mem[amount][n] != -1:
                return mem[amount][n]

            if amount == 0:
                return 1

            # zero num coins and non zero amount
            if n == 0:
                return 0
            
            not_take = 0
            take = 0
            if amount - coins[n - 1] < 0:
                not_take += check(amount, n - 1)
            else:
                take += check(amount - coins[n - 1], n)
                not_take += check(amount, n - 1)
            mem[amount][n] = take + not_take
            return mem[amount][n]
        
        res = check(amount, len(coins))
        # print(res)
        return res

        