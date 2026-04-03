class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sorted_words, ans = [], []
        anagrams_indexes = defaultdict(list)
        for word in strs:
            sorted_words.append("".join(sorted(word)))
        for i, word in enumerate(sorted_words):
            anagrams_indexes[word].append(i)
        for anagrams in anagrams_indexes:
            words = [strs[i] for i in anagrams_indexes[anagrams]]
            ans.append(words)
        return ans
        

        


        