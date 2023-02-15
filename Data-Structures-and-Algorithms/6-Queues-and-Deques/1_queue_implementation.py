class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


q = Queue()

print("Is empty:", q.isEmpty())

q.enqueue(1)
print(q.items)

q.enqueue(2)
print(q.items)

q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)

print(q.dequeue())
print(q.items)

print(q.dequeue())
print(q.items)
