class Solution:
    def isValid(self, s: str) -> bool:
        track = []
        match_dict = {
            '(': ')',
            '{' : '}',
            '[' : ']'
        }
        for c in s:
            if c in ['(', '[', '{']:
                track.append(c)
            else:
                if track and c == match_dict[track.pop()]:
                    continue
                else:
                    return False
        if len(track) == 0:
            return True
        return False

        