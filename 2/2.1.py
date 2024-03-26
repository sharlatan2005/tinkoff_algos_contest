import sys

class Stack:
    def __init__(self):
        self.buf = []
        self.min_buf = [1e9 + 1]
    
    def push(self, item):
        self.buf.append(item)
        if (item <= self.min_buf[-1]):
            self.min_buf.append(item)

    def top(self):
            return self.buf[-1]
    
    def pop(self):
        top_item = self.buf[-1]
        if (top_item == self.min_buf[-1]):
            self.min_buf = self.min_buf[:-1]
        self.buf = self.buf[:-1]
        return top_item

    def get_min(self):
        return self.min_buf[-1]
    

n = int(sys.stdin.readline())

stack = Stack()

ans = []
for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))

    if (cmd[0] == 1):
        stack.push(cmd[1])
    elif (cmd[0] == 2):
        stack.pop()
    elif (cmd[0] == 3):
        ans.append(stack.get_min())
        # print(stack.get_min(), end='\r\n')

print('\n'.join(map(str, ans)))