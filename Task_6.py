# Данные о еде
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(budget):
    # Співвідношення калорій до вартості для кожної страви
    ratio_items = [
        (item, data["calories"] / data["cost"]) for item, data in items.items()
    ]
    # Сортуємо страви за співвідношенням калорій до вартості в порядку спадання
    ratio_items.sort(key=lambda x: x[1], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, ratio in ratio_items:
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        if total_cost + cost <= budget:  # Якщо ми можемо дозволити собі цю страву
            selected_items.append(item)
            total_cost += cost
            total_calories += calories

    return selected_items, total_calories

# Динамічне програмування
def dynamic_programming(budget):
    # Массив для зберігання максимальних калорій для кожного бюджету
    dp = [0] * (budget + 1)
    # Масив для зберігання вибраних страв
    selected_items = [[] for _ in range(budget + 1)]

    # Перебір кожної страви
    for item, data in items.items():
        cost = data["cost"]
        calories = data["calories"]

        # Перебираємо всі бюджети від максимально можливого до вартості поточної страви
        for current_budget in range(budget, cost - 1, -1):
            # Якщо додаємо поточну страву дає більше калорій
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                selected_items[current_budget] = selected_items[current_budget - cost] + [item]

    return selected_items[budget], dp[budget]


# Приклад використання
budget = 100

# Виконання жадібного алгоритму
greedy_result, greedy_calories = greedy_algorithm(budget)
print(f"Жадібний алгоритм:")
print(f"Вибрані страви: {greedy_result}")
print(f"Загальна калорійність: {greedy_calories}")

# Виконання алгоритму динамічного програмування
dp_result, dp_calories = dynamic_programming(budget)
print(f"\nАлгоритм динамічного програмування:")
print(f"Вибрані страви: {dp_result}")
print(f"Загальна калорійність: {dp_calories}")
