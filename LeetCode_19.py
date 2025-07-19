class LinkedListNode:
    self.value = value
    self.next = None
    


    
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
        current = self.head
        while current.next:
            current = current.next
