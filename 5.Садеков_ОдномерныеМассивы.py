# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Лабораторная работа №5 Одномерные массивы
"""

def show_number(x):
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return x

print("Задание 1")
N=int(input("Введите размер массива N \n"))
A=[]
for i in range(N):
    A.append(2*i+1)
print("Первые N нечетных чисел", A)

print("Задание 2")
N=int(input("Введите размер массива N \n"))
A=float(input("Введите первый член A \n"))
D=float(input("Введите знаменатель D \n"))
B=[]
for i in range(N):
    B.append(A)
    A=A*D
print("Геометрическая прогрессия", [show_number(x) for x in B])

print("Задание 3")
N=int(input("Введите размер массива N \n"))
A=int(input("Введите первый элемент A \n"))
B=int(input("Введите второй элемент B \n"))
C=[A, B]
S=A+B
for i in range(2, N):
    C.append(S)
    S=S+C[-1]
print("Полученный массив", C)

print("Задание 4")
N=int(input("Введите размер массива N \n"))
A=list(map(float, input("Введите элементы массива через пробел \n").split()))
left=0
right=N-1
print("Элементы в заданном порядке:")
while left<=right:
    print(show_number(A[left]), end=" ")
    if left!=right:
        print(show_number(A[right]), end=" ")
    left=left+1
    right=right-1
print()

print("Задание 5")
N=int(input("Введите размер массива N \n"))
A=list(map(float, input("Введите элементы массива через пробел \n").split()))
print("Элементы в заданном порядке:")
for i in range(0, N, 2):
    print(show_number(A[i]), end=" ")
for i in range((N//2)*2-1, 0, -2):
    print(show_number(A[i]), end=" ")
print()

print("Задание 6")
N=int(input("Введите размер массива N \n"))
A=list(map(float, input("Введите элементы массива через пробел \n").split()))
K=int(input("Введите номер K \n"))
L=int(input("Введите номер L \n"))
S=0
for i in range(K-1, L):
    S=S+A[i]
average=S/(L-K+1)
print("Среднее арифметическое", show_number(average))

print("Задание 7")
N=int(input("Введите размер массива N \n"))
A=list(map(int, input("Введите различные целые числа через пробел \n").split()))
D=0
if N>1:
    D=A[1]-A[0]
    for i in range(2, N):
        if A[i]-A[i-1]!=D:
            D=0
            break
print("Разность прогрессии (или 0)", D)

print("Задание 8")
N=int(input("Введите размер массива N \n"))
A=list(map(float, input("Введите элементы массива через пробел \n").split()))
if N<2:
    print("Нет элементов с четными номерами")
else:
    minimum=A[1]
    for i in range(3, N, 2):
        if A[i]<minimum:
            minimum=A[i]
    print("Минимальный элемент с четным номером", show_number(minimum))

print("Задание 9")
N=int(input("Введите размер массива N \n"))
A=list(map(float, input("Введите элементы массива через пробел \n").split()))
number=0
for i in range(N):
    if (i==0 or A[i]>A[i-1]) and (i==N-1 or A[i]>A[i+1]):
        number=i+1
print("Номер последнего локального максимума", number)

print("Задание 10")
N=int(input("Введите размер массива N \n"))
A=list(map(int, input("Введите элементы массива через пробел \n").split()))
for i in range(N):
    for j in range(i+1, N):
        if A[i]==A[j]:
            print("Номера одинаковых элементов", i+1, j+1)


