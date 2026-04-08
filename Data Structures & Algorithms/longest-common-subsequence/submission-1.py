class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        mem = [ [-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]


        def check(text1, text2, m, n):



            if m == 0 or n == 0:
                return 0
            
            if mem[m][n] != -1:
                return mem[m][n]
            

            if text1[m - 1] == text2[n - 1]:
                mem[m][n] = 1 + check(text1, text2, m - 1, n - 1)
                 
            
            else:
                mem[m][n] = max(check(text1, text2, m - 1, n), 
                check(text1, text2, m, n - 1))
            return mem[m][n]

            
        return check(text1, text2, len(text1), len(text2))
        