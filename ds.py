class LinkedListNode:
    def __init__(self, data):
        self.data = data  # expects a Node object
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_node(self, node):
        new_node = LinkedListNode(node)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def remove_node(self):
        if self.head is None:
            return None
        removed_node = self.head
        self.head = self.head.next
        self.count -= 1
        return removed_node

    def num_items(self):
        return self.count


class Stack:
    def __init__(self):
        self.top = LinkedList()

    def push(self, data):
        self.top.add_node(data)

    def pop(self):
        return self.top.remove_node()

    def peek(self):
        return self.top.head.data if self.top.head else None

    def num_items(self):
        return self.top.num_items()





