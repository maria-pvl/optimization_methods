import math


def f(x):
    return (
        x * math.atan(x) - 0.5 * math.log(1 + x**2) + (2 - x) * math.log(2 - x) + x - 2
    )


x0 = 0.45
h = 0.01

f0 = f(x0)
f_left = f(x0 - h)
f_right = f(x0 + h)

print("Алгоритм Свена")
print("x0 =", x0)
print("h =", h)


if f_left < f0:
    direction = -1
elif f_right < f0:
    direction = 1
else:
    print("Мінімум знаходиться в інтервалі:")
    print("[", x0 - h, ";", x0 + h, "]")
    exit()

print("\nНапрямок:")
if direction == -1:
    print("вліво")
else:
    print("вправо")


print("\nТаблиця ітерацій:")
print("-" * 40)
print("№\t x\t f(x)")
print("-" * 40)

x1 = x0 + direction * h
f1 = f(x1)

print("0\t", round(x0, 2), "\t", round(f0, 4))
print("1\t", round(x1, 2), "\t", round(f1, 4))

i = 1

while True:

    h = h * 2

    x2 = x1 + direction * h
    f2 = f(x2)

    i = i + 1

    print(i, "\t", round(x2, 2), "\t", round(f2, 4))

    if f2 > f1:
        left = min(x0, x2)
        right = max(x0, x2)

        print("-" * 40)
        print("Інтервал локалізації мінімуму:")
        print("[", round(left, 2), ";", round(right, 2), "]")

        break

    x0 = x1
    x1 = x2
    f1 = f2
