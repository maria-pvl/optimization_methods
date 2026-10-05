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

print("Метод Ньютона")
print("Початкова точка:", x)
print("Точність:", eps)


h = 10 ** (-5)

df_num = (f(x + h) - f(x - h)) / (2 * h)

print("\nПеревірка першої похідної:")
print("f'(x) =", round(df(x), 6))
print("Чисельно =", round(df_num, 6))


print("\nТаблиця ітерацій:")
print("-" * 75)
print(
    f"{'k':<5}"
    f"{'xk':<12}"
    f"{'f(xk)':<14}"
    f"{"f'(xk)":<14}"
    f"{"|f'(xk)|":<14}"
    f"{"f''(xk)":<14}"
)
print("-" * 75)

k = 0

while True:

    fx = f(x)
    dfx = df(x)
    ddfx = ddf(x)

    print(
        f"{k:<5}"
        f"{x:<12.4f}"
        f"{fx:<14.4f}"
        f"{dfx:<14.4f}"
        f"{abs(dfx):<14.4f}"
        f"{ddfx:<14.4f}"
    )

    if abs(dfx) <= eps:
        break

    if ddfx <= 0:
        print("\nf''(x) <= 0. Метод зупинено.")
        break

    x_new = x - dfx / ddfx

    x = x_new
    k += 1


print("-" * 75)

print("\nРезультат:")
print("x_min =", round(x, 2))
print("f(x_min) =", round(f(x), 4))
print("|f'(x_min)| =", round(abs(df(x)), 4))


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
plt.title("Метод Ньютона")
plt.grid()
plt.legend()

plt.show()
