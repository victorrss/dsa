class MyStack:

    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        return self.queue.append(x)

    def pop(self) -> int:
        queue_aux = []
        while len(self.queue) > 1:
            queue_aux.append(self.queue.pop(0))
        last = self.queue.pop(0)
        self.queue = queue_aux
        return last

    def top(self) -> int:
        queue_aux = []
        while len(self.queue) != 0:
            last = self.queue.pop(0)
            queue_aux.append(last)
        self.queue = queue_aux
        return last

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
