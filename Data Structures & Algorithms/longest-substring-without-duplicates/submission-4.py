class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        l, r = 0, 1
        ans = 1
        freq_dict = defaultdict(int)
        freq_dict[s[l]] += 1

        while r < len(s):

            if freq_dict[s[r]] != 0:
                # slide window until fist duplicate is removed from window
                while freq_dict[s[r]] != 0: 
                    freq_dict[s[l]] -= 1
                    l += 1
            freq_dict[s[r]] += 1
                
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans


        