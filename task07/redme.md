# Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)

## Опис проекту

Цей проект використовує метод Монте-Карло для симуляції ймовірностей сум при киданні двох гральних кубиків. Метою є визначення ймовірностей кожної можливої суми (від 2 до 12) та порівняння отриманих результатів із аналітичними розрахунками.

Програма симулює 1 000 000 кидків двох кубиків, обчислює кількість появ кожної суми та використовує ці дані для розрахунку ймовірностей. Крім того, результати візуалізуються за допомогою графіка.

## Використання

Щоб запустити проект, виконайте наступні дії:

1. Встановіть необхідні бібліотеки:

    ```sh
    pip install matplotlib
    ```

2. Запустіть файл з кодом Python:

    ```sh
    python dice_simulation.py
    ```

## Основні функції

- `roll_dice()`: Імітує кидання двох гральних кубиків та повертає їх суму.
- Підрахунок кількості появ кожної можливої суми.
- Обчислення відсоткових ймовірностей на основі кількості симуляцій.
- Візуалізація ймовірностей у вигляді стовпчастої діаграми.

## Результати симуляції

Результати симуляції виглядають наступним чином:

| Сума | Імовірність (%) |
|------|-----------------|
| 2    | 2.87            |
| 3    | 5.56            |
| 4    | 8.38            |
| 5    | 11.06           |
| 6    | 13.75           |
| 7    | 16.71           |
| 8    | 13.95           |
| 9    | 11.09           |
| 10   | 8.39            |
| 11   | 5.50            |
| 12   | 2.73            |

## Порівняння з аналітичними ймовірностями

| Сума | Аналітична ймовірність (%) | Симуляційна ймовірність (%) |
|------|----------------------------|-----------------------------|
| 2    | 2.78                       | 2.87                        |
| 3    | 5.56                       | 5.56                        |
| 4    | 8.33                       | 8.38                        |
| 5    | 11.11                      | 11.06                       |
| 6    | 13.89                      | 13.75                       |
| 7    | 16.67                      | 16.71                       |
| 8    | 13.89                      | 13.95                       |
| 9    | 11.11                      | 11.09                       |
| 10   | 8.33                       | 8.39                        |
| 11   | 5.56                       | 5.50                        |
| 12   | 2.78                       | 2.73                        |

Результати симуляції досить близькі до аналітичних значень, що підтверджує правильність використання методу Монте-Карло. Невеликі відхилення є наслідком випадкового характеру симуляцій, проте вони залишаються в межах очікуваної похибки.

## Висновки

Метод Монте-Карло є ефективним способом для оцінки ймовірностей подій, де теоретичні обчислення можуть бути складними або недоступними. У випадку кидання двох кубиків, аналітичні ймовірності збігаються з результатами симуляцій, що підтверджує коректність теоретичних розрахунків.

Проект показує, як велика кількість симуляцій (1 000 000) дозволяє досягти високої точності результатів, де похибки між аналітичними і симуляційними значеннями залишаються незначними.
