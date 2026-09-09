import math


def f(x):
    return (
        x * math.atan(x) - 0.5 * math.log(1 + x**2) + (2 - x) * math.log(2 - x) + x - 2
    )


a = 0.45
b = 0.48
eps = 0.01


print("Метод половинного поділу")
print("Початковий інтервал: [", a, ";", b, "]")
print("Точність:", eps)

print("\nТаблиця ітерацій:")
print("-" * 70)
print("№\t a\t b\t x\t f(x)")
print("-" * 70)

i = 1


while (b - a) > eps:

    x = (a + b) / 2

    x1 = (a + x) / 2
    x2 = (x + b) / 2

    f1 = f(x1)
    f2 = f(x2)

    print(
        i,
        "\t",
        round(a, 2),
        "\t",
        round(b, 2),
        "\t",
        round(x, 2),
        "\t",
        round(f(x), 4),
    )

    if f1 < f2:
        b = x2
    else:
        a = x1

    i += 1


x_min = (a + b) / 2
f_min = f(x_min)


print("-" * 70)
print("Кінцевий інтервал:")
print("[", round(a, 2), ";", round(b, 2), "]")

print("\nТочка мінімуму:")
print("x_min =", round(x_min, 2))

print("\nМінімальне значення функції:")
print("f(x_min) =", round(f_min, 4))
