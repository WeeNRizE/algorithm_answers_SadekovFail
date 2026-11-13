# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Лабораторная работа №6 Двумерные массивы
"""

def show_number(x):
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return x

print("Задание 1")
M=int(input("Введите нечетный порядок матрицы M \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
top=0
bottom=M-1
left=0
right=M-1
print("Элементы по спирали против часовой стрелки:")
while top<=bottom:
    for i in range(top, bottom+1):
        print(show_number(A[i][left]), end=" ")
    for j in range(left+1, right+1):
        print(show_number(A[bottom][j]), end=" ")
    for i in range(bottom-1, top-1, -1):
        print(show_number(A[i][right]), end=" ")
    for j in range(right-1, left, -1):
        print(show_number(A[top][j]), end=" ")
    top=top+1
    bottom=bottom-1
    left=left+1
    right=right-1
print()

print("Задание 2")
M=int(input("Введите количество строк M \n"))
N=int(input("Введите количество столбцов N \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
K=int(input("Введите номер строки K \n"))
S=0
P=1
for j in range(N):
    S=S+A[K-1][j]
    P=P*A[K-1][j]
print("Сумма элементов строки", show_number(S))
print("Произведение элементов строки", show_number(P))

print("Задание 3")
M=int(input("Введите количество строк M \n"))
N=int(input("Введите количество столбцов N \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
min_product=None
column=0
for j in range(N):
    P=1
    for i in range(M):
        P=P*A[i][j]
    if min_product is None or P<min_product:
        min_product=P
        column=j+1
print("Номер столбца", column)
print("Минимальное произведение", show_number(min_product))

print("Задание 4")
M=int(input("Введите количество строк M \n"))
N=int(input("Введите количество столбцов N \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
for j in range(N):
    S=0
    for i in range(M):
        S=S+A[i][j]
    average=S/M
    count=0
    for i in range(M):
        if A[i][j]>average:
            count=count+1
    print("Столбец", j+1, "Количество элементов", count)

print("Задание 5")
M=int(input("Введите количество строк M \n"))
N=int(input("Введите количество столбцов N \n"))
A=[]
for i in range(M):
    A.append(list(map(int, input("Введите строку матрицы через пробел \n").split())))
number=0
for j in range(N):
    all_odd=True
    for i in range(M):
        if A[i][j]%2==0:
            all_odd=False
            break
    if all_odd:
        number=j+1
        break
print("Номер первого столбца с нечетными элементами", number)

print("Задание 6")
M=int(input("Введите количество строк M \n"))
N=int(input("Введите количество столбцов N \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
for i in range(M):
    min_index=A[i].index(min(A[i]))
    max_index=A[i].index(max(A[i]))
    A[i][min_index], A[i][max_index]=A[i][max_index], A[i][min_index]
print("Измененная матрица:")
for row in A:
    print(*(show_number(x) for x in row))

print("Задание 7")
M=int(input("Введите количество строк M \n"))
N=int(input("Введите количество столбцов N \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
minimum=A[0][0]
maximum=A[0][0]
min_col=0
max_col=0
for i in range(M):
    for j in range(N):
        if A[i][j]<minimum:
            minimum=A[i][j]
            min_col=j
        if A[i][j]>maximum:
            maximum=A[i][j]
            max_col=j
for i in range(M):
    A[i][min_col], A[i][max_col]=A[i][max_col], A[i][min_col]
print("Матрица после обмена столбцов:")
for row in A:
    print(*(show_number(x) for x in row))

print("Задание 8")
M=int(input("Введите четное количество строк M \n"))
N=int(input("Введите четное количество столбцов N \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
for i in range(M//2):
    for j in range(N//2):
        A[i][j], A[i+M//2][j+N//2]=A[i+M//2][j+N//2], A[i][j]
print("Матрица после обмена четвертей:")
for row in A:
    print(*(show_number(x) for x in row))

print("Задание 9")
M=int(input("Введите количество строк M \n"))
N=int(input("Введите количество столбцов N \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
for i in range(M-1):
    for j in range(i+1, M):
        if A[i][0]>A[j][0]:
            A[i], A[j]=A[j], A[i]
print("Матрица с отсортированными строками:")
for row in A:
    print(*(show_number(x) for x in row))

print("Задание 10")
M=int(input("Введите порядок квадратной матрицы M \n"))
A=[]
for i in range(M):
    A.append(list(map(float, input("Введите строку матрицы через пробел \n").split())))
for d in range(1-M, M):
    S=0
    for i in range(M):
        j=i-d
        if 0<=j<M:
            S=S+A[i][j]
    print("Сумма диагонали", d+M, "=", show_number(S))