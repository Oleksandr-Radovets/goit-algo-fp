import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def monte_carlo_dice_rolls(num_rolls):
    sums = {i: 0 for i in range(2, 13)}  # Суми від 2 до 12

    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)  # Результат першого кубика
        die2 = random.randint(1, 6)  # Результат другого кубика
        total_sum = die1 + die2      # Сума
        sums[total_sum] += 1         # Підрахунок кількості кожної суми

    # Обчислення ймовірностей для кожної суми
    probabilities = {key: value / num_rolls for key, value in sums.items()}

    return sums, probabilities

# Симуляція
num_rolls = 100000  # Кількість кидків
sums, probabilities = monte_carlo_dice_rolls(num_rolls)

# Аналітичні ймовірності
analytic_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}

# Виведення результатів
print("Ймовірності за методом Монте-Карло:")
for sum_value in range(2, 13):
    print(f"Сума {sum_value}: {probabilities[sum_value]:.4f}")

print("\nАналітичні ймовірності:")
for sum_value in range(2, 13):
    print(f"Сума {sum_value}: {analytic_probabilities[sum_value]:.4f}")

# Графік ймовірностей
x = list(range(2, 13))
y_monte_carlo = [probabilities[i] for i in x]
y_analytic = [analytic_probabilities[i] for i in x]

plt.bar(x, y_monte_carlo, width=0.4, label='Монте-Карло', alpha=0.6)
plt.bar([i + 0.4 for i in x], y_analytic, width=0.4, label='Аналітичні', alpha=0.6)

plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
plt.legend()
plt.show()