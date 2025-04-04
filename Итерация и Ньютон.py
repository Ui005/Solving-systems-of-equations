import math

#пример: 3lnx^2 + 6lnx - 5 = 0
#отрезок: [1;3]


def simple_iterattion(x):
    global c_s
    global epsilon
    c_s += 1
    x_old = x
    x = math.exp((5-3*math.log(x)**2)/6)

    if abs(x - x_old) < epsilon:
        return x
    else:
        return simple_iterattion(x)

def method_newton(x):
    global c_n
    global epsilon
    c_n += 1
    x_old = x
    f = 3 * math.log(x)**2 + 6 * math.log(x) - 5
    df = (6 * math.log(x) + 6) / x
    x = x_old - f / df

    if abs(x - x_old) < epsilon:
        return x
    else:
        return method_newton(x)


epsilon = 0.0001
c_s = 0
c_n = 0
x0 = 2

result1 = simple_iterattion(x0)
result2 = method_newton(x0)
print("Решение после ", c_s, " итераций (методом простых итераций):", result1)
print("Решение после ", c_n, " итераций (методом Ньютона):", result2)
print(result1 - result2)