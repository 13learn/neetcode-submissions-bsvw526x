class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            # in left sorted array
            if nums[m] >= nums[l]:
                if nums[m] >= target:
                    if nums[l] <= target:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    # target is bigger than mid as all elements on th left are smaller than mid due to left sorted array
                    l = m + 1
            # in right sorted array
            else:
                if nums[m] <= target:
                    if nums[r] >= target:
                        l = m + 1
                    else:
                        r = m - 1
                
                else:
                    r = m - 1
        return -1



        