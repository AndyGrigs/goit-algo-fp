items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["cost"] / x[1]["calories"], reverse=True)
    total_calories = 0
    selected_items = []

    for item, data in sorted_items:
        if budget >= data["cost"]:
            selected_items.append(item)
            budget -= data["cost"]
            total_calories += data["calories"]

    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        item_name, item_data = item_list[i - 1]
        cost = item_data['cost']
        calories = item_data['calories']
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    # Визначаємо, які страви були обрані
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item_name = item_list[i - 1][0]
            selected_items.append(item_name)
            b -= item_list[i - 1][1]['cost']

    total_calories = dp[n][budget]
    return selected_items, total_calories

# Приклад використання
budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_result[0])
print("Сумарна калорійність:", greedy_result[1])

dp_result = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Обрані страви:", dp_result[0])
print("Сумарна калорійність:", dp_result[1])