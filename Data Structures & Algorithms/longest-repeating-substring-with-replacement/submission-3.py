class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            freq_dict = {}
            for j in range(i, len(s)):
                freq_dict[s[j]] = 1 + freq_dict.get(s[j], 0)
                max_freq = max(list(freq_dict.values()))

                if (j - i + 1) - max_freq <= k:
                    res = max(res, j - i + 1)
                    continue
                break

        return res


        