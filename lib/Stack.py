class Stack:

    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            # raise Exception("Stack is full.")
            return

    def pop(self):
        if self.size() != 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        pass

    def size(self):
        return len(self.items)

    def full(self):
        return self.size() == self.limit

    def search(self, target):
        if target in self.items:
            return self.size() - self.items.index(target) - 1
        else:
            return -1
