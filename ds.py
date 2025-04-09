class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0  # num_items için sayaç

    def add_node(self, node):
        node.next = self.head
        self.head = node
        self.count += 1

    def remove_node(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        self.count -= 1
        return removed

    def num_items(self):
        return self.count

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




