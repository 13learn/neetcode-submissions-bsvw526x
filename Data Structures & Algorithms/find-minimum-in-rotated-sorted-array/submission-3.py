class Solution:
    def findMin(self, nums: List[int]) -> int:
        s , e = 0, len(nums) - 1
        ans = nums[0]
        
        while s <= e:
            m = s + (e - s) // 2

            if nums[s] <= nums[e]:
                ans = min(ans, nums[s])
                break
            ans = min(ans, nums[m])
            
            
            if nums[m] >= nums[s]:
                s = m + 1  # min present in right subarray

            else:
                e = m - 1
            
        return ans

                


        