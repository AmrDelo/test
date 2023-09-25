class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Empty Queue"
    def is_empty(self):
        return len(self.items) == 0
    def print_queue(self):
        for ele in self.items:
            print(ele)
    def queue_size(self):
        return len(self.items)
q = queue()
q.enqueue(20)
q.enqueue(30)
removed = q.dequeue()
print("Removed ",removed)
q.enqueue(40)
q.enqueue(50)
print("Queue size ",q.queue_size())
print("Queue Items ")
q.print_queue()