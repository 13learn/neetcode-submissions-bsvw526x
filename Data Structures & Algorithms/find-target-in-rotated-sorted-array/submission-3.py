def findMin(nums: List[int]) -> int:
    l , r = 0, len(nums) - 1

    if not nums:
        return -1
    min_idx = 0
    while l <= r:
        m = l + (r - l) // 2
        if nums[l] < nums[r]:
            min_idx = l
            break
        if nums[m] < nums[min_idx]:
            min_idx = m
        if nums[m] >= nums[l]:
            l = m + 1
        
        else:
            r = m - 1

    return min_idx

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if nums[0] < nums[-1]:
            l = 0
            r = len(nums) - 1
        else:
            min_idx = findMin(nums)
            print(min_idx)

            if nums[min_idx] == target:
                return min_idx

            if target >= nums[0]:
                # target is present in left sorted array
                l = 0
                r = min_idx
            else:
                l = min_idx
                r = len(nums) - 1
        
        while l <= r:

            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            if target >= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return -1

        