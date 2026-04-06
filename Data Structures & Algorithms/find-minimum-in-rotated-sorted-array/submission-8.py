class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1

        if not nums:
            return -1
        ans = nums[0]
        while l <= r:
            m = l + (r - l) // 2
            print(l , r, m)
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            ans = min(ans, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            
            else:
                r = m - 1
        
        return ans
        
        