class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.nums = []
        self.minS = []

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
            self.minS.append(val)
        self.nums.append(val) 

    def pop(self) -> None:
        ch = self.nums.pop()
        if ch == self.minS[-1]:
            self.minS.pop()

    def top(self) -> int:
        return self.nums[-1] 

    def getMin(self) -> int:
        return self.minS[-1]
