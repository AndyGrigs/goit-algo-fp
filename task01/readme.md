# Linked List

Цей файл містить реалізацію списку зв'язку на мові Python. Список зв'язку - це лінійна структура даних, де кожен елемент (названий вузол) вказує на наступний вузол у списку.

## Класи

### `Node`

Клас `Node` представляє окремий вузол у списку. Він має дві атрибути: `data` та `next`. Атрибут `data` зберігає значення вузла, а атрибут `next` зберігає посилання на наступний вузол у списку.

### `LinkedList`

Клас `LinkedList` представляє самий список. Він має наступні методи:

- `__init__`: Ініціалізує новий список.
- `append`: Додає новий вузол у кінець списку.
- `print_list`: Виводить елементи списку.
- `reverse`: Зворотній список.
- `insertion_sort`: Сортує список за допомогою алгоритму вставки.
- `_sorted_insert`: Допоміжна функція для алгоритму вставки.
- `merge_sorted_lists`: Об'єднує два відсортованих списку у один відсортований список.

## Приклад використання

Ось приклад використання класу `LinkedList`:

```python
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(2)
print("Оригінальний список 1:")
list1.print_list()

list1.reverse()
print("Зворотній список 1:")
list1.print_list()

list1.insertion_sort()
print("Сортований список 1:")
list1.print_list()

list2 = LinkedList()
list2.append(4)
list2.append(5)
print("Оригінальний список 2:")
list2.print_list()

merged_list = LinkedList.merge_sorted_lists(list1, list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()