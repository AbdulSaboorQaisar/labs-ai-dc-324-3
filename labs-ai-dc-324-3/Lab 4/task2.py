# Question:2
# Implement Queue using Python.

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.front())   
print(queue.size())  