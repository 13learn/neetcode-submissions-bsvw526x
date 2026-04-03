class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        char_count = [0] * 256 
        l = 0

        for r in range(len(s)):
            while char_count[ord(s[r])] >= 1:
                char_count[ord(s[l])] -= 1
                l += 1
            char_count[ord(s[r])] += 1
            ans = max(ans, r - l + 1)

        return ans   

        