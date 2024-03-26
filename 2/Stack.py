class ToppingEmptyStack(Exception):
    def __init__(self, message):
        super().__init__(message)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def isEmpty(self):
        return len(self.stack) == 0
    
    def top(self):
        if (not self.isEmpty()):
            return self.stack[-1]
        else:
            raise(ToppingEmptyStack("Failed when accesing the top element of an empty stack"))

    def pop(self):
        try:
            last_item = self.top()
        except ToppingEmptyStack as e:
            print(e.message)
        self.stack = self.stack[:-1]
        return last_item

    def getMin(self):
        buf = Stack()
        min_item = self.top()
        while (not self.isEmpty()):
            top_item = self.pop()
            min_item = min(min_item, top_item)
            buf.push(top_item)
        while (not buf.isEmpty()):
            self.push(buf.pop())
        return min_item
