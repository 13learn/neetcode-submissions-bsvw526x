class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0

        while l <= r:
            rem_cap = limit - people[r]
            ans += 1
            r -= 1

            if people[l] <= rem_cap:
                l += 1
        
        return ans
        