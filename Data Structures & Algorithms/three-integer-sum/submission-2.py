class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twosum(target, skip):
            l, r = 0, len(nums) - 1

            sub_ans = []
            
            while l < r:

                if l == skip:
                    l += 1
                    continue
                
                if r == skip:
                    r -= 1
                    continue
                
                if nums[l] + nums[r] == target:
                    triplet = [nums[l], nums[r], -target]
                    triplet.sort()
                    sub_ans.append(triplet)
                    r -= 1
                    l += 1
                    continue
                    

                if nums[l] + nums[r] > target:
                    r -= 1
                
                elif nums[l] + nums[r] < target:
                    l += 1
            return sub_ans

        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            curren_match = twosum(target, i)
            for match in curren_match:
                ans.add(tuple(match))
        
        final_ans = [list(trip) for trip in ans]
        
        return final_ans

             

        