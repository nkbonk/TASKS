class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_at_position(head, value, pos):
    new_node = LinkedListNode(value)

    if pos <= 0 or not head:
        new_node.next = head
        return new_node

    cur = head
    for _ in range(pos - 1):
        if not cur.next:
            break
        cur = cur.next

    new_node.next = cur.next
    cur.next = new_node
    return head 
