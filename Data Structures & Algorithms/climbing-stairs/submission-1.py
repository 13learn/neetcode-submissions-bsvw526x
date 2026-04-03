class Solution:
    def climbStairs(self, n: int) -> int:
        possible_ways = [0] * (n + 1)
        possible_ways[0] = 1
        possible_ways[1] = 1

        for i in range(2, n + 1):
            possible_ways[i] = possible_ways[i - 1] + possible_ways[i - 2]
        return possible_ways[-1]

        