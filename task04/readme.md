# Візуалізація бінарної купи

Цей проєкт надає Python-скрипт для візуалізації бінарної купи як дерева за допомогою бібліотек `networkx` та `matplotlib`. Візуалізація допомагає зрозуміти структуру бінарної купи, представленої у вигляді бінарного дерева.

## Можливості

- Перетворює бінарну купу, представлену масивом, у структуру бінарного дерева.
- Візуалізує бінарне дерево за допомогою `networkx` та `matplotlib`.
- Підтримує налаштування кольорів вузлів та значень для кращої візуалізації.

## Файли

- `heap_visualization.py`: Містить реалізацію візуалізації бінарної купи.
- `readme.md`: Документація для розуміння та використання скрипта.

## Функції

### Клас Node

```python
class Node:
    def __init__(self, key, color="skyblue"):
```
- Представляє вузол у бінарному дереві.
- Атрибути:
  - `key`: Значення вузла.
  - `color`: Колір вузла для візуалізації (за замовчуванням "skyblue").
  - `id`: Унікальний ідентифікатор для кожного вузла.

### Функція add_edges

```python
def add_edges(graph, node, pos, x=0, y=0, layer=1):
```
- Рекурсивно додає вузли та ребра до графа для візуалізації.
- Параметри:
  - `graph`: Граф, до якого додаються вузли та ребра.
  - `node`: Поточний вузол, який додається.
  - `pos`: Словник для відстеження позицій кожного вузла для побудови.
  - `x`, `y`: Координати для розміщення вузлів.
  - `layer`: Поточна глибина вузла в дереві.
- Використовує `x - 1 / 2 ** layer` і `x + 1 / 2 ** layer` для визначення позицій лівих і правих нащадків відповідно.

### Функція draw_tree

```python
def draw_tree(tree_root):
```
- Малює бінарне дерево за допомогою `networkx` та `matplotlib`.
- Параметри:
  - `tree_root`: Кореневий вузол бінарного дерева.
- Використовує кольори вузлів та мітки для покращення візуалізації.

### Функція heap_to_tree

```python
def heap_to_tree(heap):
```
- Перетворює бінарну купу (представлену у вигляді масиву) у структуру бінарного дерева.
- Параметри:
  - `heap`: Список, що представляє бінарну купу.
- Повертає кореневий вузол бінарного дерева.
- Використовує індекси масиву для встановлення зв'язків між батьківськими та дочірніми вузлами.

## Приклад використання

```python
# Приклад бінарної купи
heap = [10, 5, 8, 3, 2, 7, 6]

# Перетворення купи у бінарне дерево
root = heap_to_tree(heap)

# Візуалізація бінарного дерева
draw_tree(root)
```

## Вимоги

- Python 3.x
- `networkx`
- `matplotlib`

Встановіть необхідні бібліотеки за допомогою:

```sh
pip install networkx matplotlib
```

## Як запустити

1. Склонуйте репозиторій або скопіюйте скрипт.
2. Встановіть необхідні залежності.
3. Запустіть скрипт для візуалізації бінарної купи:

```sh
python heap_visualization.py
```

## Ліцензія

Цей проєкт ліцензовано за ліцензією MIT.