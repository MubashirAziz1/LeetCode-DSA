class MinStack:

    def __init__(self):
        self.stack = []
        self.minst = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val , self.minst[-1] if self.minst else val)
        self.minst.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0:
          self.stack.pop()
          self.minst.pop()
        else:
          return "Stack is Empty"

    def top(self) -> int:
        if len(self.stack) != 0:
          return self.stack[-1]
        else:
         return "Stack is Empty" 

    def getMin(self) -> int:
        if len(self.stack) != 0
          return self.minst[-1]
        else:
          return "Stack is Empty" 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
