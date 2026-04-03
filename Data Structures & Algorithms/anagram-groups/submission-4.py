class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for word in strs:
            key = [0] * 26

            for c in word:
                key[ord(c) - ord('a')] += 1
            

            anagrams_dict[tuple(key)].append(word)
        
        return list(anagrams_dict.values())


        