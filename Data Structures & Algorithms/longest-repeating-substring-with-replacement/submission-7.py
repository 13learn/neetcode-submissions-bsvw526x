class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0

        ans = 1
        l, r = 0, 0
        from collections import defaultdict
        freq = defaultdict(int)
        while r < len(s):
            freq[s[r]] += 1

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans


        