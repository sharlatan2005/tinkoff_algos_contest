from collections import deque

class Queue():
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()
        self.stack_stor = deque()
    def push(self, item):
        self.stack1.append(item)
    def top(self):
        if (len(self.stack2) == 0):
            return self.stack1[0]
        else:
            return self.stack2[-1]
    def pop(self):
        if (len(self.stack2) == 0):
            while (len(self.stack1) > 0):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def pop_end(self):
        if (len(self.stack1) == 0):
            last = self.stack2[-1]
            self.stack2 = self.stack2[1:]
            return last
        else:
            return self.stack1.pop()
    def get_number_in_front(self, item):
        cnt = 0
        while (self.top() != item):
            self.stack_stor.append(self.pop())
            cnt += 1
        while (len(self.stack_stor) > 0):
            self.stack2.append(self.stack_stor.pop())
        return cnt
        

    