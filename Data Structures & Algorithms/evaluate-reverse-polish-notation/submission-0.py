class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        ops = ['+', '-', '/', '*']
        for c in tokens:
            if c in ops:
                if c=='+':
                    x1 = int(res.pop())
                    x2 = int(res.pop())
                    res.append(x1+x2)
                elif c == '-':
                    x1 = int(res.pop())
                    x2 = int(res.pop())
                    res.append(x2-x1)
                elif c == '*':
                    x1 = int(res.pop())
                    x2 = int(res.pop())
                    res.append(x1*x2)
                elif c == '/':
                    x1 = int(res.pop())
                    x2 = int(res.pop())
                    res.append(int(x2/x1))
            else:
                res.append(int(c))
        return res[0]