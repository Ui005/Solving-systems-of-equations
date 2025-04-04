

def simple_iter(x1,x2,x3,x4):
    global c
    c += 1
    # Сохраняем предыдущие значения
    x1_old, x2_old, x3_old, x4_old = x1, x2, x3, x4
    # Пересчитываем приближения
    x1 = (176 - 7 * x3_old - 5 * x4_old) / 15
    x2 = (-111 + 3 * x1_old + 6 * x3_old - x4_old) / -14
    x3 = (74 + 2 * x1_old - 9 * x2 + 2 *x4_old) / 13
    x4 = (76 - 4 * x1_old + x2_old - 3 * x3_old) / 9
    # Проверка условий останова
    diff = max(abs(x1 - x1_old), abs(x2 - x2_old), abs(x3 - x3_old), abs(x4 - x4_old))
    if diff < epsilon:
        return x1, x2, x3, x4
    else:
        return simple_iter(x1, x2, x3, x4)

# Начальное приближение
x1, x2, x3, x4 = 0.0, 0.0, 0.0, 0.0

# Точность
epsilon = 0.001

# Счётчик итераций
c = 0

x1, x2, x3, x4 = simple_iter(x1, x2, x3, x4)
print(f"Решение после {c} итераций:")
print("x1 = ", x1)
print("x2 = ", x2)
print("x3 = ", x3)
print("x4 = ", x4)

"""
Решение после 9 итераций:
x1 = 8.84555868999704
x2 = 4.863032907604919
x3 = 3.384470591951799
x4 = 3.9254176651141304
"""
