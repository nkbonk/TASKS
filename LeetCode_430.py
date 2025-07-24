class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        if not head:
            return None

        cur = head
        list = []

        while cur:
            if cur.child:
                if cur.next:
                    list.append(cur.next)
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None

            if not cur.next and list:
                temp = list.pop()
                cur.next = temp
                temp.prev = cur
            cur = cur.next

        return head
