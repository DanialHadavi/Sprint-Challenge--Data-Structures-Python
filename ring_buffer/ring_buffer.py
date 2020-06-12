class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        self.advance()

    def advance(self):
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        buffer = [item for item in self.storage if item is not None]
        return buffer
