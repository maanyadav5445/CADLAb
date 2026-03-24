queue = []

def enqueue(x):
    queue.append(x)

def dequeue():
    if queue:
        return queue.pop(0)
    return None

for i in range(5):
    enqueue(i * 2)

print(queue)

while queue:
    print(dequeue())