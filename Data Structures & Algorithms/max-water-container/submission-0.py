class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):

            for j in range(i, len(heights)):

                area = min(heights[i], heights[j]) * (j - i)
                ans = max(ans, area)
        
        return ans

        