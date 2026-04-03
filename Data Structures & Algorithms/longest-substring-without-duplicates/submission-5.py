class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans = 0, 0
        f = defaultdict(int)

        r = 0

        while r < len(s):

            while f[s[r]] > 0:
                f[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
            f[s[r]] += 1
            r += 1

        return ans        