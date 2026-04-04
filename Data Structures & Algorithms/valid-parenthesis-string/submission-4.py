class Solution:
    def checkValidString(self, s: str) -> bool:

        l_min, l_max = 0, 0

        i = 0

        while i < len(s) and l_max >= 0:

            if s[i] == "(":
                l_min += 1
                l_max += 1
            elif s[i] == ")":
                l_min = max(0, l_min - 1)
                l_max -= 1
            else:
                l_min = max(0, l_min - 1)
                l_max += 1
            i += 1
        print(l_min, l_max)
        if l_min == 0 and l_max >= 0:
            return True
        return False




            
        


        