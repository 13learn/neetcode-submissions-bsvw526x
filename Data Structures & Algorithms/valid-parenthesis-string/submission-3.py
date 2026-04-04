class Solution:
    def checkValidString(self, s: str) -> bool:

        dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        
        def check(s, idx, count):

            if count < 0:
                return False
            if idx == len(s):
                return (count == 0)

            if dp[idx][count] is not None:
                return dp[idx][count]
 
            if s[idx] == '(':
                result = check(s, idx + 1,  count + 1)
            elif s[idx] == ')':
                result = check(s, idx + 1, count - 1)
            else:
                result = (check(s, idx + 1,  count + 1) or 
                check(s, idx + 1, count - 1) or 
                check(s, idx + 1, count))
    
            dp[idx][count] = result
            return result
        
        return check(s, 0, 0)





            
        


        