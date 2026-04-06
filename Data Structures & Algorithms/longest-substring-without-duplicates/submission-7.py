class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0

        freq = defaultdict(int)

        while r < len(s):

            while freq[s[r]] > 0 :
                
                freq[s[l]] -= 1
                l += 1
            
            freq[s[r]] += 1
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans



        