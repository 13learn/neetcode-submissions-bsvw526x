class Solution:
    def isValid(self, s: str) -> bool:
        paran_map = {')':'(', '}':'{', ']':'['}
        paranthesis_stack = []
        for c in s:
            # open paranthesis case
            if c not in paran_map:
                paranthesis_stack.append(c)
            else:
                if not paranthesis_stack:
                    return False
                top_element = paranthesis_stack.pop()
                if top_element != paran_map[c]:
                    return False
        return not len(paranthesis_stack)

        