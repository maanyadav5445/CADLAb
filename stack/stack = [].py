stack = []

def push(x):
    stack.append(x)

def pop():
    if stack:
        return stack.pop()
    return None

def peek():
    if stack:
        return stack[-1]
    return None

for i in range(5):
    push(i)

print(stack)

while stack:
    print(pop())

print(peek())