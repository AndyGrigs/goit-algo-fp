# """
# 1.написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# 2.розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# 3.написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
# """


# Клас для вузла однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data  # Зберігає значення вузла
        self.next = None  # Посилання на наступний вузол у списку, яке спочатку є None

# Клас для роботи з однозв'язним списком
class LinkedList:
    def __init__(self):
        self.head = None  # Початок списку, спочатку порожній (None)

    # Функція для додавання нового елемента в кінець списку
    def append(self, data):
        new_node = Node(data)  # Створюємо новий вузол
        if not self.head:      # Якщо список порожній, встановлюємо новий вузол як голову списку
            self.head = new_node
            return
        current = self.head
        while current.next:    # Проходимо до кінця списку
            current = current.next
        current.next = new_node  # Додаємо новий вузол у кінець

    # Функція для друку всіх елементів списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 1. Функція для реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next    # Зберігаємо посилання на наступний вузол
            current.next = prev         # Змінюємо напрямок посилання
            prev = current              # Переміщаємо prev на поточний вузол
            current = next_node         # Переходимо до наступного вузла
        self.head = prev                # Встановлюємо нову голову списку

    # 2. Алгоритм сортування вставками для однозв'язного списку
    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next                # Зберігаємо посилання на наступний вузол
            sorted_list = self._sorted_insert(sorted_list, current)  # Вставка у відсортований список
            current = next_node                     # Переходимо до наступного вузла
        self.head = sorted_list                     # Встановлюємо відсортований список як головний

    # Допоміжна функція для вставки вузла у відсортований список
    def _sorted_insert(self, head, node):
        if not head or node.data < head.data:  # Вставка на початок, якщо список порожній або data менше, ніж у голови
            node.next = head
            return node
        current = head
        while current.next and current.next.data < node.data:
            current = current.next            # Пошук місця для вставки
        node.next = current.next              # Вставка вузла у потрібне місце
        current.next = node
        return head

    # 3. Функція для об'єднання двох відсортованих однозв'язних списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node(0)      # Тимчасовий вузол для зручності
        tail = dummy
        l1 = list1.head
        l2 = list2.head

        while l1 and l2:     # Поки є вузли в обох списках
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Приєднуємо решту вузлів, якщо в одному зі списків вони залишилися
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        merged_list = LinkedList()
        merged_list.head = dummy.next   # Переносимо голову нового списку
        return merged_list

# Приклад використання
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(2)
print("Оригінальний список 1:")
list1.print_list()

# Реверсування списку
list1.reverse()
print("Реверсований список 1:")
list1.print_list()

# Сортування списку
list1.insertion_sort()
print("Відсортований список 1:")
list1.print_list()

# Створення другого списку
list2 = LinkedList()
list2.append(4)
list2.append(5)
print("Оригінальний список 2:")
list2.print_list()

# Об'єднання двох відсортованих списків
merged_list = LinkedList.merge_sorted_lists(list1, list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
