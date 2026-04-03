class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        freq_map = defaultdict(list)

        for word in strs:
            
            key = [0] * 26

            for c in word:
                key[ord(c) - ord('a')] += 1
            
            freq_map[tuple(key)].append(word)
        
        return list(freq_map.values())
        