import turtle

# Функція для малювання дерева Піфагора
def draw_tree(length, level, angle, t):
    if level == 0:
        return
    else:
        # Малюємо основну лінію
        t.forward(length)

        # Малюємо праву гілку
        t.left(angle)
        draw_tree(length * 0.7, level - 1, angle, t)

        # Повертаємося до початкової позиції
        t.right(2 * angle)
        draw_tree(length * 0.7, level - 1, angle, t)

        # Повертаємо кінець до початкового положення
        t.left(angle)
        t.backward(length)

# Налаштовуємо вікно та черепаху для малювання
def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.backward(200)  # Зміщуємо черепаху вліво, щоб дерево не виходило за межі екрану
    t.pendown()

    # Вказуємо довжину початкової лінії, рівень рекурсії і кут
    length = 100  # Початкова довжина
    level = int(input("Введіть рівень рекурсії: "))  # Користувач може вказати рівень
    angle = 30  # Кут розгалуження

    draw_tree(length, level, angle, t)

    # Закриваємо вікно при натисканні
    screen.exitonclick()

if __name__ == "__main__":
    main()
