class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        
        bracket_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        for c in s:
            if c in bracket_map:
                stack.append(c)
                continue

            if len(stack) <= 0:
                return False

            val = stack.pop()
            bracket = bracket_map.get(val)

            if bracket == None:
                return False
            elif bracket != c:
                return False
        
        if len(stack) > 0:
            return False

        return True