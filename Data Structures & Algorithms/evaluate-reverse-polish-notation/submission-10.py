import math as m

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op = {"+","-","/","*"}

        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                match token:
                    case '+':
                       res = first + second
                    case "-":
                        res = first - second
                    case "*":
                        res = first * second
                    case "/":
                        print(first, second)
                        res = int(first / second)
                stack.append(res)
        
        return stack[0]