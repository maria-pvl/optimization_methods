import math


def f(x):
    return (
        x * math.atan(x) - 0.5 * math.log(1 + x**2) + (2 - x) * math.log(2 - x) + x - 2
    )


a = 0.45
b = 0.48
eps = 0.01

phi = (math.sqrt(5) - 1) / 2


print("Метод золотого перерізу")
print("Початковий інтервал: [", a, ";", b, "]")
print("Точність:", eps)

print("\nТаблиця ітерацій:")
print("-" * 120)
print("№\t x1\t\t x2\t\t f(x1)\t\t f(x2)\t\t [a, b]\t\t\t L")
print("-" * 120)


i = 1

x1 = b - phi * (b - a)
x2 = a + phi * (b - a)

f1 = f(x1)
f2 = f(x2)


while (b - a) > eps:

    L = b - a

    print(
        i,
        "\t",
        round(x1, 4),
        "\t",
        round(x2, 4),
        "\t",
        round(f1, 4),
        "\t",
        round(f2, 4),
        "\t",
        "[",
        round(a, 4),
        ";",
        round(b, 4),
        "]",
        "\t",
        round(L, 4),
    )

    if f1 < f2:
        b = x2
        x2 = x1
        f2 = f1
        x1 = b - phi * (b - a)
        f1 = f(x1)
    else:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a + phi * (b - a)
        f2 = f(x2)

    i += 1


x_min = (a + b) / 2
f_min = f(x_min)


print("-" * 120)
print("Кінцевий інтервал:")
print("[", round(a, 2), ";", round(b, 2), "]")

print("\nТочка мінімуму:")
print("x_min =", round(x_min, 2))

print("Мінімальне значення функції:")
print("f(x_min) =", round(f_min, 4))
