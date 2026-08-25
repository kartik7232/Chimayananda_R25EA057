class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class list:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def show(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        if elements:
            print(" -> ".join(elements))
        else:
            print("Empty List")