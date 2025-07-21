class MyLinkedList(object):
    class MyLinkedListNode:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.length = 0



    def get(self, index):
        if index < 0 or index >= self.length:
            return -1
        i = 0
        current = self.head

        while i != index:
            current = current.next
            i += 1
        return current.val



    def addAtHead(self, val):
        new_node = self.MyLinkedListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    


    def addAtTail(self, val):
        new_node = self.MyLinkedListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
        


    def addAtIndex(self, index, val):
        if index <= 0:
            new_node = self.MyLinkedListNode(val)
            new_node.next = self.head
            self.head = new_node
            self.length += 1

        elif index == self.length:
            new_node = self.MyLinkedListNode(val)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
            self.length += 1

        elif 0 < index < self.length:
            i = 0
            current = self.head
            while i != index - 1:
                current = current.next
                i += 1
            new_node = self.MyLinkedListNode(val)
            new_node.next = current.next
            current.next = new_node
            self.length += 1



    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next

        else:
            i = 0
            current = self.head
            while i != index - 1:
                current = current.next
                i += 1
            current.next = current.next.next
        self.length -= 1
