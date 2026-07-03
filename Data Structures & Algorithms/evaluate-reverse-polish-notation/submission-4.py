class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        opSet = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in opSet:
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

            
