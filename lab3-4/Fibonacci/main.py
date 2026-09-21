import math


def f(x):
    return (
        x * math.atan(x) - 0.5 * math.log(1 + x**2) + (2 - x) * math.log(2 - x) + x - 2
    )


a = 0.45
b = 0.48
eps = 0.01
delta = eps / 10


print("Метод чисел Фібоначчі")
print("Початковий інтервал: [", a, ";", b, "]")
print("Точність:", eps)


F = [1, 1]

while F[-1] < (b - a) / eps:
    F.append(F[-1] + F[-2])

N = len(F) - 1


print("\nЧисла Фібоначчі:")
print(F)

print("N =", N)


print("\nТаблиця ітерацій:")
print("-" * 100)
print("k\t x1\t x2\t f(x1)\t\t f(x2)\t\t [a, b]\t\t\t L")
print("-" * 100)

for k in range(N - 2):

    m = N - k

    if m > 3:
        x1 = a + F[m - 2] / F[m] * (b - a)
        x2 = a + F[m - 1] / F[m] * (b - a)

    else:
        x1 = a + (b - a) / 2
        x2 = x1 + delta

    f1 = f(x1)
    f2 = f(x2)

    L = b - a

    print(
        k,
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

    if f1 <= f2:
        b = x2
    else:
        a = x1


x_min = (a + b) / 2
f_min = f(x_min)


print("-" * 100)

print("Кінцевий інтервал:")
print("[", round(a, 2), ";", round(b, 2), "]")

print("\nТочка мінімуму:")
print("x_min =", round(x_min, 2))

print("\nМінімальне значення функції:")
print("f(x_min) =", round(f_min, 4))
