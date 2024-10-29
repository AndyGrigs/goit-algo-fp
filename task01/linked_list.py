"""
1.написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
2.розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
3.написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # Початок списку, спочатку порожній (None)
        
    def append(self, data):
        new_node = Node(data)
        if not self.next:
            self.next = new_node
            return
        current = self.next
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head