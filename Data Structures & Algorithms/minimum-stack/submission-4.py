class MinStack:

    def __init__(self):
        self.stack = []
        self.m = None
        

    def push(self, val: int) -> None:
        if self.m == None:
            self.m = val
        elif val < self.m:
            self.m = val
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.m = None
        else:
            s = sorted(self.stack)
            self.m = sorted(s)[0]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m
        
