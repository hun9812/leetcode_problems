class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print(stack, token)
            try:
                token = int(token)
                stack.append(token)
            except:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
        return stack[0]