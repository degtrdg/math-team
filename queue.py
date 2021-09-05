class node():
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prev = None
 
 
class queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def enqueue(self, item):
        new_node = node(item)
        if(self.size == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
 
    def dequeue(self):
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        if (self.size == 0):
            self.tail = None
        return x
 
    def front(self):
        return self.head.item
 
    def isEmpty(self):
        if(self.size == 0):
            return True
        return False
