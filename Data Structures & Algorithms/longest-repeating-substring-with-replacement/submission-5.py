class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans, r = 0, 0, 0
        f = defaultdict(int)

        while r < len(s):
            f[s[r]] += 1
            while (r - l + 1) - max(f.values()) > k:
                f[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

            r += 1
            
        
        return ans