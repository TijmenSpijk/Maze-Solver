class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def count(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(self.count() - 1)

    def count(self):
        return len(self.items)