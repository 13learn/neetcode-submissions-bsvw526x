class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_element = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:

            if nums[r] > nums[l]:
                min_element = min(min_element, nums[l])
                break
            
            m = l + (r - l) // 2
            min_element = min(min_element, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return min_element
        