def gauss_elimination(matrix, b, n):
    for i in range(n):

        # Поиск строки с максимальным ведущим элементом
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        # Перестановка строк
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        b[i], b[max_row] = b[max_row], b[i]

        if matrix[0][0] == 0:  # Проверка ведущего элемента,если он 0,
            return None        # то решения либо нет,либо их бесконечно много


# Обнуление элементов под ведущим элементом
        for j in range(i + 1, n):
            coeff = matrix[j][i]/matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= matrix[i][k] * coeff
            b[j] -= coeff * b[i]

# Нахождение решения
    x = [0]*n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]
    return x

n = int(input('Введите размерность матрицы коэффицентов(кол-во уравнений): '))
n = 4
matrix = [
    [15, 0, 7, 5],
    [-3, -14, -6, 1],
    [-2, 9, 13, 1],
    [4, -1, 3, 9]
]
b = [176,-111,74,76]
matrix = []
b = []

for i in range(n):
    print('Ведите через пробел коэффициенты уравнения ', i + 1, ':')
    line = list(map(float, input().split()))
    if len(line) != n:
        print("Ошибка! Неверное кол-во коэффициентов.")
    else:
        matrix.append(line)

print('Введите через пробел свободные члены уравнения: ')
b = (list(map(float, input().split())))

# Решение системы
solution = gauss_elimination(matrix, b, n)

# Вывод результата
if solution:
    print("Решение системы:")
    for i in range(n):
        print("x", i+1, "= ", solution[i])
else:
    print("Система не имеет решений или имеет бесконечно много решений.")

    """
Решение системы:
x 1 =  8.84546118276953
x 2 =  4.862983694329521
x 3 =  3.3845217814553417
x 4 =  3.9252859576539305
    """