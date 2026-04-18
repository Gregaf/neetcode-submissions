class Solution:
    def isValid(self, s: str) -> bool:
        # ( { [

        stack = []

        correlation_map = { ")": "(", "]": "[", "}": "{"}
        opening_bracket = correlation_map.values()
        for c in s:
            if c in opening_bracket:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                curr = stack.pop()

                expected_bracket = correlation_map.get(c)

                if curr is not expected_bracket:
                    return False
        
        return len(stack) == 0
            
