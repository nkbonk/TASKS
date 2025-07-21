def reverse_list(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

head = ListNode(1, ListNode(2, ListNode(3)))
res = reverse_list(head)
while res:
    print(res.val, end=' ')
