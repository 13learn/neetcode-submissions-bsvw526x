class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        work = []

        for token in tokens:

            if token not in ["+", "-", "/", "*"]:
                work.append(token)
                continue

            second = int(work.pop())
            first = int(work.pop())
            res = 0
            if token == "+":
                res = first + second
                
            elif token == "*":
                res = first * second
            elif token == "-":
                res = first - second
            elif token == "/":
                res = first / second
            work.append(res)
        return int(work[0])
        