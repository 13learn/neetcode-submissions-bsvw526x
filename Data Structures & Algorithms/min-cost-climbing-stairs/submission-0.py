class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        ans = [0] * (len(cost) + 1)
        ans[0], ans[1] = 0, 0

        for i in range(2, len(cost) + 1):

            ans[i] = min(cost[i - 2] + ans[i - 2],
            cost[i - 1] + ans[i - 1])
            # print(i, ans[i])
        
        return ans[-1]
        