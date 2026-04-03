class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        l = 0
        freq_dict = defaultdict(int)
        ans = 0
        for r in range(len(s)):
            freq_dict[s[r]] += 1
            while (r - l + 1) - max(freq_dict.values()) > k:
                freq_dict[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
        