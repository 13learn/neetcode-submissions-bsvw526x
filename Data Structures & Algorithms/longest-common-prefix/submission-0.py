class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = len(min(strs))
        ans = ""

        for i in range(min_len):
            cur_set = set()
            for str in strs:
                cur_set.add(str[i])
            
            if len(cur_set) != 1:
                break
            ans += list(cur_set)[0]
        
        return ans

        