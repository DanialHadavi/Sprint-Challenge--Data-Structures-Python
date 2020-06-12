from dll import DoublyLinkedList
import sys
sys.path.append('../dll')


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size <= 0:
            return None
        self.size -= 1
        value = self.storage.remove_from_head()
        return value

    def len(self):
        return self.size
