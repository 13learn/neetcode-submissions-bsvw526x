class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        deposit = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 5:
                deposit[5] += 1
                continue
            elif bill == 10 and deposit[5] > 0:
                deposit[5] -= 1
                deposit[10] += 1
                continue
            elif bill == 20 and deposit[5] > 0 and deposit[10] > 0:
                deposit[5] -= 1
                deposit[10] -= 1
                deposit[20] += 1
                continue
            elif bill == 20 and deposit[5] > 2:
                deposit[5] -= 3
                deposit[20] += 1
                continue
            return False
        return True




        