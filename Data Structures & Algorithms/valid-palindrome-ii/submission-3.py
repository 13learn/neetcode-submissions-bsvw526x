class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() for c in s if c.isalnum()])

        del_count = 0

        i, j = 0, len(s) - 1

        def is_palin(i, j):

            while i < j:

                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while i < j:

            if s[i] != s[j]:

                return is_palin(i + 1 ,j) or is_palin(i ,j - 1)
            i += 1
            j -= 1
        
        return True
            
            
        