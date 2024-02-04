class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.val=val
        return self.stack.append(self.val)

    def pop(self) -> None:
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
       return min(self.stack[0::])


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()