import math
import matplotlib.pyplot as plt


def f(x):
    return (
        x * math.atan(x) - 0.5 * math.log(1 + x**2) + (2 - x) * math.log(2 - x) + x - 2
    )


def df(x):
    return math.atan(x) - math.log(2 - x)


def ddf(x):
    return 1 / (1 + x**2) + 1 / (2 - x)


x = 0.35

eps = 0.001
alpha = 0.5
t_min = 0


print("Метод Ньютона-Рафсона")
print("Початкова точка:", x)
print("Точність:", eps)
print("alpha =", alpha)
print("t_min =", t_min)


h = 10 ** (-5)

df_num = (f(x + h) - f(x - h)) / (2 * h)

print("\nПеревірка першої похідної:")
print("f'(x) =", round(df(x), 6))
print("Чисельно =", round(df_num, 6))


print("\nТаблиця ітерацій:")
print("-" * 125)

print(
    f"{'k':<5}"
    f"{'xk':<12}"
    f"{'f(xk)':<14}"
    f"{"f'(xk)":<14}"
    f"{"f''(xk)":<14}"
    f"{'t':<10}"
    f"{'x_bar':<14}"
    f"{'f(x_bar)':<14}"
    f"{"f'(x_bar)":<14}"
)

print("-" * 125)


k = 0

while True:

    fx = f(x)
    dfx = df(x)
    ddfx = ddf(x)

    if abs(dfx) <= eps:

        print(f"{k:<5}" f"{x:<12.4f}" f"{fx:<14.4f}" f"{dfx:<14.4f}" f"{ddfx:<14.4f}")

        break

    if ddfx <= 0:
        print("\nf''(x) <= 0. Метод зупинено.")
        break

    t = 1

    while True:

        x_bar = x - t * dfx / ddfx

        df_bar = df(x_bar)

        if abs(df_bar) <= eps:

            f_bar = f(x_bar)

            print(
                f"{k:<5}"
                f"{x:<12.4f}"
                f"{fx:<14.4f}"
                f"{dfx:<14.4f}"
                f"{ddfx:<14.4f}"
                f"{t:<10.4f}"
                f"{x_bar:<14.4f}"
                f"{f_bar:<14.4f}"
                f"{df_bar:<14.4f}"
            )

            x = x_bar
            break

        f_bar = f(x_bar)

        right_side = -alpha * t * dfx**2 / ddfx

        left_side = f_bar - fx

        print(
            f"{k:<5}"
            f"{x:<12.4f}"
            f"{fx:<14.4f}"
            f"{dfx:<14.4f}"
            f"{ddfx:<14.4f}"
            f"{t:<10.4f}"
            f"{x_bar:<14.4f}"
            f"{f_bar:<14.4f}"
            f"{df_bar:<14.4f}"
        )

        if left_side <= right_side:
            x = x_bar

            break

        t = t / 2

        if t < t_min:

            print("\nt < t_min.")
            print("Дроблення кроку не допомогло.")
            print("Пошук зупинено.")

            print("\nРезультат:")
            print("x_min =", round(x, 6))
            print("f(x_min) =", round(f(x), 6))

            exit()

    ddf_new = ddf(x)

    k += 1


print("-" * 125)

print("\nРезультат:")
print("x_min =", round(x, 6))
print("f(x_min) =", round(f(x), 6))
print("|f'(x_min)| =", round(abs(df(x)), 6))


x0_graph = 0.35

x1_graph = x0_graph - df(x0_graph) / ddf(x0_graph)

x2_graph = x1_graph - df(x1_graph) / ddf(x1_graph)

x_values = []

start = 0.2
end = 0.8

step = (end - start) / 200

x_graph = start

while x_graph <= end:
    x_values.append(x_graph)
    x_graph += step


phi_values = []

for x_graph in x_values:
    phi_values.append(df(x_graph))


tangent1 = []

for x_graph in x_values:

    y = df(x0_graph) + ddf(x0_graph) * (x_graph - x0_graph)

    tangent1.append(y)


tangent2 = []

for x_graph in x_values:

    y = df(x1_graph) + ddf(x1_graph) * (x_graph - x1_graph)

    tangent2.append(y)


plt.plot(x_values, phi_values, label="φ(x) = f'(x)")

plt.plot(x_values, tangent1, label="Дотична 1-ї ітерації")

plt.plot(x_values, tangent2, label="Дотична 2-ї ітерації")

plt.scatter([x0_graph, x1_graph], [df(x0_graph), df(x1_graph)], label="Точки ітерацій")

plt.axhline(0)

plt.xlabel("x")
plt.ylabel("φ(x)")
plt.title("Метод Ньютона-Рафсона")
plt.grid()
plt.legend()

plt.show()
