class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = {"(":")", "{":"}","[":"]"}
        closeBrackets = {")":"(","}":"{","]":"["}

        for c in s:
            if len(stack) == 0 and c in closeBrackets:
                return False
            if c in openBrackets:
                stack.append(c)
            else:
                if stack[-1] == closeBrackets[c]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
