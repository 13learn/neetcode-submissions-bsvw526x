class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [0] * len(nums)
        postfix_prod = [0] * len(nums)
        prefix_prod[0] = 1
        postfix_prod[-1] = 1
        for i in range(1, len(nums)):
            prefix_prod[i] = prefix_prod[i - 1] * nums[i - 1]
        # print(prefix_prod)
        
        for i in range(len(nums) - 2, -1, -1):
            postfix_prod[i] = postfix_prod[i + 1] * nums[i + 1]
        # print(postfix_prod)
        for i in range(len(nums)):
            postfix_prod[i] = postfix_prod[i] * prefix_prod[i]
        return postfix_prod
        