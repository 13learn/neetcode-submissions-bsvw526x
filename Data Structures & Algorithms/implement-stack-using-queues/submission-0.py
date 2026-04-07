class MyStack:

    def __init__(self):
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()
        
        

    def push(self, x: int) -> None:
        if not self.q1 and not self.q2:
            # first element
            self.q1.append(x)
            return
        if self.q1:
            self.q2.append(x)
            while self.q1:
                ele = self.q1.popleft()
                self.q2.append(ele)
        else:
            self.q1.append(x)
            while self.q2:
                ele = self.q2.popleft()
                self.q1.append(ele)

    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()
        else:
            return self.q2.popleft()


    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        else:
            return self.q2[0]
        

    def empty(self) -> bool:
        if self.q1 or self.q2:
            return False
        return True
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()