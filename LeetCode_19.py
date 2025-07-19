class LinkedListNode:
    self.value = value
    self.next = None
    
    def remove_Nth_from_end(head: ListNode, n: int):   # Содержимое в скобках написала нейронка, чтобы леткод не ругался (не помогло)
        dummy = LinkedListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next
    
    
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
