class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        def isOp(string: str):
            return string=="+" or string=="-" or string=="*" or string=="/"
        for token in tokens:
            if isOp(token):
                num1 = numStack.pop()
                num2 = numStack.pop()
                if token == "+":
                    numStack.append(num2 + num1)
                elif token == "-":
                    numStack.append(num2 - num1)
                elif token == "*":
                    numStack.append(num2 * num1)
                else:
                    numStack.append(int(num2/num1))
            else:
                numStack.append(int(token))
        return numStack.pop()

            
