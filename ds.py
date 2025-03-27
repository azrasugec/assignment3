class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        node.next = self.head
        self.head = node

    def remove_node(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        return removed

class Stack:
    def __init__(self):
        self.top = LinkedList()

    def push(self, data):
        node = LinkedListNode(data)
        self.top.add_node(node)

    def pop(self):
        return self.top.remove_node()

    def peek(self):
        return self.top.head



