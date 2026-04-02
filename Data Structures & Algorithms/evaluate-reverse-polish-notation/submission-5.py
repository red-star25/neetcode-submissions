class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for s in tokens:
            if s == '+':
                n1 = res.pop()
                n2 = res.pop()
                res.append(n1 + n2)
            
            elif s == "-":
                n1 = res.pop()
                n2 = res.pop()
                res.append(n2 - n1)

            elif s == "*":
                n1 = res.pop()
                n2 = res.pop()
                res.append(n1 * n2)
            
            elif s == "/":
                n1 = res.pop()
                n2 = res.pop()
                res.append(int(float(n2)/n1))
            
            else:
                res.append(int(s))
        
        return res[0]