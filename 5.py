def reverseList(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

head = ListNode(1, ListNode(2, ListNode(3)))
res = reverseList(head)
while res:
    print(res.val, end=' ')
