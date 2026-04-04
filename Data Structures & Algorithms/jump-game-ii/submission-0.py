class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            win = 0 # current window

            for i in range(l, r + 1):
                win = max(win, i + nums[i])
            
            l = r + 1
            r = win
            jumps += 1
        
        return jumps
        