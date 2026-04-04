class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = {}

        def check(dp, idx):

            if idx == len(s):
                return True
            
            if idx in dp: return dp[idx]

            for word in wordDict: # k
                end_idx = idx + len(word)
                # O(L)
                if s[idx:end_idx] == word: 
                    if check(dp, end_idx):
                        dp[end_idx] = True
                        return True
            dp[end_idx] = False

                    
            return False
        
        return check(dp, 0)


