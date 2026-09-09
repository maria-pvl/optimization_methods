import math


def f(x):
    return (
        x * math.atan(x) - 0.5 * math.log(1 + x**2) + (2 - x) * math.log(2 - x) + x - 2
    )


a = 0.45
b = 0.48
eps = 0.01
delta = 0.001

print("Метод дихотомії")
print("Початковий інтервал: [", a, ";", b, "]")
print("Точність:", eps)

print("\nТаблиця ітерацій:")
print("-" * 90)
print("№\t a\t b\t x1\t x2\t f(x1)\t f(x2)")
print("-" * 90)

i = 0

while (b - a) > eps:

    x1 = (a + b) / 2 - delta
    x2 = (a + b) / 2 + delta

    f1 = f(x1)
    f2 = f(x2)

    print(
        i,
        "\t",
        round(a, 2),
        "\t",
        round(b, 2),
        "\t",
        round(x1, 2),
        "\t",
        round(x2, 2),
        "\t",
        round(f1, 4),
        "\t",
        round(f2, 4),
    )

    if f1 < f2:
        b = x2
    else:
        a = x1

    i += 1


x_min = (a + b) / 2
f_min = f(x_min)

print("-" * 90)
print("Кінцевий інтервал:")
print("[", round(a, 2), ";", round(b, 2), "]")

print("\nТочка мінімуму:")
print("x_min =", round(x_min, 2))

print("Мінімальне значення функції:")
print("f(x_min) =", round(f_min, 4))
