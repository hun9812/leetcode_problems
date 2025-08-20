class MyQueue:

    def __init__(self):
        self.s1_for_print = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s2.append(x)
        

    def pop(self) -> int:
        if not self.s1_for_print:
            while self.s2:
                temp = self.s2.pop()
                self.s1_for_print.append(temp)
        return self.s1_for_print.pop()

    def peek(self) -> int:
        if not self.s1_for_print:
            while self.s2:
                temp = self.s2.pop()
                self.s1_for_print.append(temp)
        return self.s1_for_print[len(self.s1_for_print)-1]

    def empty(self) -> bool:
        if not self.s1_for_print:
            if not self.s2:
                return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()