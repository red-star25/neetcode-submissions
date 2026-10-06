class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+","-","*","/"}
        stack = []

        for token in tokens:
            if token not in op:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                match token:
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num1 - num2)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(num1 / num2)
        
        return int(stack[0])
