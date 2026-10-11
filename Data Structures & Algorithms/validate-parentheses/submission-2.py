class Solution:
    def isValid(self, s: str) -> bool:
        stck = []

        opposite = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for val in s:
            if val in opposite:
                stck.append(val)
            else:
                if not stck:
                    return False

                last = stck.pop()

                if opposite[last] != val:
                    return False

        return len(stck) == 0