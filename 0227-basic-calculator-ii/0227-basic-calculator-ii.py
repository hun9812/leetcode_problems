class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        def find_num(i):
            while i < len(s) and s[i] == " ":
                i += 1

            n = ""
            while i < len(s) and s[i] in "0123456789":
                n += s[i]
                i += 1
            return int(n),i

        while i < len(s):
            if s[i] == " ":
                i += 1
                continue

            if s[i] in "0123456789":
                n, i = find_num(i)
                stack.append(n)
                continue
            if s[i] == "*":
                i += 1
                n2, i = find_num(i)
                n1 = stack.pop()
                stack.append(n1*n2)
            elif s[i] == "/":
                i += 1
                n2, i = find_num(i)
                n1 = stack.pop()
                stack.append(int(n1/n2))
            else:
                stack.append(s[i])
                i += 1
        
        stack = stack[::-1]
        while len(stack) > 1:
            a1 = stack.pop()
            f = stack.pop()
            a2 = stack.pop()
            if f == "+":
                stack.append(a1+a2)
            elif f == "-":
                stack.append(a1-a2)
        
        return stack[0]
