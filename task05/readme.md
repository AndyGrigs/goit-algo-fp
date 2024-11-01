# Специфікація: Візуалізація обходу бінарного дерева

## Опис завдання
Необхідно створити програму на Python, яка будує та візуалізує бінарне дерево з заданого масиву. Програма повинна виконувати два види обходу дерева:
1. Обхід у глибину (in-order).
2. Обхід у ширину (breadth-first).

Під час обходу кожен вузол змінює свій колір, відображаючи порядок відвідування. Кольори змінюються від темних до світлих відтінків, щоб візуально передати послідовність обходу.

## Вимоги

### Вхідні дані
- Вхідні дані — це масив `heap`, який представляє структуру бінарного дерева.

### Логіка реалізації
1. **Створення дерева:**
   - Написати функцію `heap_to_tree(heap)`, яка перетворює масив `heap` на структуру бінарного дерева.
   - Вузли мають властивості: значення (`val`), лівий (`left`) і правий (`right`) дочірні вузли, колір (`color`) та унікальний ідентифікатор (`id`).

2. **Візуалізація дерева:**
   - Написати функцію `draw_tree(tree_root, visited_nodes_colors)`, яка малює дерево з використанням бібліотеки `networkx` та `matplotlib`.
   - Вузли дерева відображаються у вигляді графу з унікальними кольорами, які змінюються при кожному відвідуванні вузла під час обходу.

3. **Обхід у глибину:**
   - Реалізувати функцію `traverse_in_order(node, visited, colors)`, яка виконує обхід у глибину (in-order).
   - Функція зберігає порядок відвідування вузлів і змінює їх кольори залежно від порядку обходу.

4. **Обхід у ширину:**
   - Реалізувати функцію `traverse_breadth_first(root, colors)`, яка виконує обхід у ширину.
   - При кожному кроці функція змінює колір вузла та відображає дерево, використовуючи градієнт кольорів для показу послідовності відвідувань.

5. **Генерація кольорів:**
   - Написати функцію `generate_color_gradient(n)`, яка створює градієнт кольорів від темних до світлих відтінків для заданої кількості кроків `n`.

### Функціонал
- Програма змінює кольори вузлів при обході, поступово змінюючи відтінки від темного до світлого.
- Кожен крок обходу відображається на графі для кращого розуміння порядку обходу.