import math
import matplotlib.pyplot as plt


def f(x):
    return (
        x * math.atan(x) - 0.5 * math.log(1 + x**2) + (2 - x) * math.log(2 - x) + x - 2
    )


x1 = 0.35

delta = 0.1

sigma_f = 0.01
sigma_x = 0.001

x2 = round(x1 + delta, 10)

f1 = f(x1)
f2 = f(x2)

if f1 > f2:
    x3 = round(x1 + 2 * delta, 10)
else:
    x3 = round(x1 - delta, 10)

if x3 <= 0:
    print("x3 <= 0. Зменшіть крок delta.")
    exit()

f3 = f(x3)


x1_start = x1
x2_start = x2
x3_start = x3

f1_start = f1
f2_start = f2
f3_start = f3


print("Метод Пауелла")
print("Початкові точки:", x1, x2, x3)
print("Крок:", delta)
print("Точність по f:", sigma_f)
print("Точність по x:", sigma_x)


print("\nТаблиця ітерацій:")
print("-" * 125)
print("k\t x1\t x2\t x3\t f(x1)\t\t f(x2)\t\t f(x3)\t\t x~\t\t f(x~)")
print("-" * 125)


k = 1
Nf = 3

first_x_new = None
first_f_new = None


while True:

    if f1 <= f2 and f1 <= f3:
        xmin = x1
        fmin = f1
    elif f2 <= f1 and f2 <= f3:
        xmin = x2
        fmin = f2
    else:
        xmin = x3
        fmin = f3

    if f1 >= f2 and f1 >= f3:
        xmax = x1
        fmax = f1
    elif f2 >= f1 and f2 >= f3:
        xmax = x2
        fmax = f2
    else:
        xmax = x3
        fmax = f3

    a1 = (f2 - f1) / (x2 - x1)

    a2 = (((f3 - f1) / (x3 - x1)) - a1) / (x3 - x2)

    if a2 > 0:
        x_new = -a1 / (2 * a2) + (x1 + x2) / 2
    else:
        x_new = 2 * xmin - xmax

    x_new = round(x_new, 10)

    if x_new == x1 or x_new == x2 or x_new == x3:
        print("x~ збігається з існуючою точкою.")
        break

    f_new = f(x_new)
    Nf += 1

    if k == 1:
        first_x_new = x_new
        first_f_new = f_new

    print(
        k,
        "\t",
        round(x1, 2),
        "\t",
        round(x2, 2),
        "\t",
        round(x3, 2),
        "\t",
        round(f1, 4),
        "\t",
        round(f2, 4),
        "\t",
        round(f3, 4),
        "\t",
        round(x_new, 4),
        "\t",
        round(f_new, 4),
    )

    if abs(fmin - f_new) <= sigma_f and abs(xmin - x_new) <= sigma_x:
        break

    if f1 >= f2 and f1 >= f3:
        x1 = x_new
        f1 = f_new

    elif f2 >= f1 and f2 >= f3:
        x2 = x_new
        f2 = f_new

    else:
        x3 = x_new
        f3 = f_new

    k += 1


print("-" * 125)

print("Кількість обчислень f:", Nf)

print("\nТочка мінімуму:")
print("x_min =", round(x_new, 2))

print("\nМінімальне значення функції:")
print("f(x_min) =", round(f_new, 4))


a1_start = (f2_start - f1_start) / (x2_start - x1_start)

a2_start = (((f3_start - f1_start) / (x3_start - x1_start)) - a1_start) / (
    x3_start - x2_start
)


x_graph = []

start = x1_start - 0.05
end = x3_start + 0.05

step = (end - start) / 100

x = start

while x <= end:
    x_graph.append(x)
    x += step


y_function = []

for x in x_graph:
    y_function.append(f(x))


y_parabola = []

for x in x_graph:
    y = (
        f1_start
        + a1_start * (x - x1_start)
        + a2_start * (x - x1_start) * (x - x2_start)
    )

    y_parabola.append(y)


plt.plot(x_graph, y_function, label="f(x)")

plt.plot(x_graph, y_parabola, label="Парабола першої ітерації")

plt.scatter(
    [x1_start, x2_start, x3_start],
    [f1_start, f2_start, f3_start],
    label="Початкові точки",
)

plt.scatter([first_x_new], [first_f_new], label="x~")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Метод Пауелла")
plt.grid()
plt.legend()

plt.show()
