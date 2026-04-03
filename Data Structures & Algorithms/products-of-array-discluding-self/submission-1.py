class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        zeros = 0
        prod = 1
        for num in nums:
            if num == 0 and zeros == 0:
                zeros += 1
                continue
            prod *= num
        
        if zeros > 1:
            return ans
        
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = [0] * len(nums)
                ans[i] = int(prod)
                return ans
            ans[i] = int(prod / nums[i])
        
        return ans

            
        