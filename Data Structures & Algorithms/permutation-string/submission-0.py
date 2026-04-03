class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        if len(s2) < window_size:
            return False
        s1_freq_dict = defaultdict(int)
        s2_freq_dict = defaultdict(int)
        for c in s1:
            s1_freq_dict[c] += 1
        l = 0
        r = window_size - 1
        #create for first window
        for i in range(window_size - 1):
            s2_freq_dict[s2[i]] += 1
        while r < len(s2):
            s2_freq_dict[s2[r]] += 1
            current_window = s2[l:r + 1]
            all_same = 0
            for c, count in s1_freq_dict.items():
                if s2_freq_dict[c] == count:
                    all_same += 1
            if all_same == window_size:
                return True
            s2_freq_dict[s2[l]] -= 1
            l += 1
            r += 1
            
        return False




        