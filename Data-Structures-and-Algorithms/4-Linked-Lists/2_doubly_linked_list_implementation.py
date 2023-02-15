class Doubly_Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


a = Doubly_Node(1)
b = Doubly_Node(2)
c = Doubly_Node(3)

a.next = b
b.prev = a

b.next = c
c.prev = b

print(b.prev.value)
print(c.prev.value)
print(a.next.next.value)
