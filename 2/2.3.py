from collections import deque

stack = deque()

expr = input().rstrip().split()

operations = ["+", "-", "*"]

for i in expr:
    if i not in operations:
        stack.append(i)
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        if (i == "+"):
            stack.append(a + b)
        elif(i == "-"):
            stack.append(a - b)
        elif(i == "*"):
            stack.append(a * b)

print(stack.pop())