class Solution:
    def isValid(self, s: str) -> bool:
        paranthesisMap = {"{": "}", "[": "]", "(": ")"}

        stack = []

        for paranthesis in s:
            if paranthesis in paranthesisMap:
                stack.append(paranthesis)
            else:
                if stack and paranthesisMap[stack[-1]]==paranthesis:
                    stack.pop()
                else:
                    return False

        return not stack
