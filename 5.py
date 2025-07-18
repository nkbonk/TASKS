# GPT написал
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev 
