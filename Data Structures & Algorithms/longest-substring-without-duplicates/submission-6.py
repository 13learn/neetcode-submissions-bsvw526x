class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = 1
        l, r = 0, 0
        from collections import defaultdict
        freq = defaultdict(int)

        while r < len(s):

            freq[s[r]] += 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans
        