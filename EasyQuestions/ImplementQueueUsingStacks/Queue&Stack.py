class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

class MyQueue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def push(self, x: int) -> None:
        self.input.push(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if self.output.isEmpty():
            while self.input.isEmpty() == False:
                self.output.append(self.input.pop())
        return self.output.peek()

    def empty(self) -> bool:
        return self.input.isEmpty() and self.output.isEmpty()

    def size(self):
        return self.stack.size() + self.stack.size()