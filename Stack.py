class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
s = Stack()
s.push('a')
s.push('b')
print(s.get_stack())
s.pop()
print(s.get_stack())
s.pop()
s.pop()
print(s.peek())