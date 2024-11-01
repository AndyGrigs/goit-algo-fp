import random
import matplotlib.pyplot as plt

# Функція для імітації кидання двох кубиків
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

# Кількість симуляцій
num_simulations = 100000

# Підрахунок появи кожної суми
counts = {i: 0 for i in range(2, 13)}

# Проведення симуляцій
for _ in range(num_simulations):
    result = roll_dice()
    counts[result[0] + result[1]] += 1

# Обчислення ймовірностей для кожної суми
probs = {key: (value / num_simulations) * 100 for key, value in counts.items()}

# Виведення результатів
print("Сума\tІмовірність")
for sum_value, probability in probs.items():
    print(f"{sum_value}\t{probability:.2f}%")

# Побудова графіка
sums = list(probs.keys())
probabilities = list(probs.values())

plt.bar(sums, probabilities)
plt.xlabel('Сума')
plt.ylabel('Імовірність (%)')
plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Аналітичні ймовірності для порівняння
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
    8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Порівняння аналітичних та симуляційних ймовірностей
print("\nПорівняння аналітичних та симуляційних ймовірностей:")
print("Сума\tАналітична\tСимуляційна")
for sum_value in sums:
    analytical = analytical_probabilities[sum_value]
    simulation = probs[sum_value]
    print(f"{sum_value}\t{analytical:.2f}%\t{simulation:.2f}%")
