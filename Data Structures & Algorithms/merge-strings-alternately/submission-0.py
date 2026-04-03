class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        ans = ""
        for i in range(min_len):
            ans += word1[i] + word2[i]
        
        ans += word1[min_len:] + word2[min_len:]

        return ans
        