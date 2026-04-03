class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        from collections import defaultdict
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        for c in t:
            count[c] -= 1
        
        for n in count:
            if count[n] != 0:
                return False
                
        return True
        