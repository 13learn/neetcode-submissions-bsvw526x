class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        first_row = nums[:len(nums) - 1]
        second_row = nums[1:]

        first_money = [0] * len(first_row)
        second_money = [0] * len(second_row)

        first_money[0] = first_row[0]
        first_money[1] = max(first_row[0], first_row[1])

        for i in range(2, len(first_row)):
            first_money[i] = max(first_money[i - 1], 
            first_row[i] + first_money[i - 2])
        
        second_money[0] = second_row[0]
        second_money[1] = max(second_row[0], second_row[1])

        for i in range(2, len(second_row)):
            second_money[i] = max(second_money[i - 1], 
            second_row[i] + second_money[i - 2])
        
        return max(first_money[-1], second_money[-1])
        



        