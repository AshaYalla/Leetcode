class MinStack:

    def __init__(self):
        self.queue = []
        self.minn = []
        

    def push(self, val: int) -> None:
        if len(self.queue) == 0:
            self.minn.append(val)
        if self.minn[-1] >= val:
            self.minn.append(val)
        self.queue.append(val)
        

    def pop(self) -> None:
        x = self.queue.pop()
        if(self.minn[-1] == x):
            self.minn.pop()
        return x
        

    def top(self) -> int:
        return self.queue[-1]
        

    def getMin(self) -> int:
        print(self.minn)
        return self.minn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()