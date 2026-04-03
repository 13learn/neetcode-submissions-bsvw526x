class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        ans = 0
        maxf = 0
        freq_count = {}

        for r in range(len(s)):

            freq_count[s[r]] = 1 + freq_count.get(s[r], 0)
            maxf = max(maxf, freq_count[s[r]])

            while (r - l + 1) - maxf > k:
                freq_count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1
        return ans


        