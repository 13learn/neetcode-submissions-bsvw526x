class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        for word in strs:
            characters_count = [0]*26
            for c in word:
                characters_count[ord(c)-ord('a')] += 1
            ans[tuple(characters_count)].append(word)
        return ans.values()

        

        


        