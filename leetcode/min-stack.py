class MinStack:
    # Time: O(1)
    # Space: O(n)

    # Initialize two stacks
    def __init__(self):
        self.stack = []        
        self.minStack = []
    
    def push(self, val: int) -> None:
        # add value to stack
        self.stack.append(val)
        # add minimum value between current and the one already there to minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        # add value to minStack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # the value on top would be the minimum value in the stack
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()