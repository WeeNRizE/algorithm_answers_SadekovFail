# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Лабораторная работа №3 Циклические алгоритмы
"""

print("Задание 1")
a=float(input("Введите цену 1 кг конфет \n"))
for i in range(1, 11):
    k=i/10
    S=a*k
    print("Стоимость", k, "кг конфет", round(S, 2))

print("Задание 2")
N=int(input("Введите целое число N \n"))
P=1
for i in range(1, N+1):
    P=P*(1+i/10)
print("Произведение", P)

print("Задание 3")
N=int(input("Введите целое число N \n"))
S=0
for i in range(1, N+1):
    S=S+(2*i-1)
    print("Текущая сумма", S)
print("Квадрат числа", S)

print("Задание 4")
A=float(input("Введите число A \n"))
N=int(input("Введите целое число N \n"))
S=1
P=1
for i in range(1, N+1):
    P=P*A
    S=S+P
print("Сумма", S)

print("Задание 5")
A=float(input("Введите число A \n"))
N=int(input("Введите целое число N \n"))
S=1
P=1
for i in range(1, N+1):
    P=P*(-A)
    S=S+P
print("Значение выражения", S)

print("Задание 6")
A=int(input("Введите целое число A \n"))
B=int(input("Введите целое число B \n"))
for i in range(A, B+1):
    for j in range(i):
        print(i, end=" ")
    print()

print("Задание 7")
A=float(input("Введите длину отрезка A \n"))
B=float(input("Введите длину отрезка B \n"))
while A>=B:
    A=A-B
print("Длина незанятой части отрезка", round(A, 10))

print("Задание 8")
N=int(input("Введите целое число N \n"))
K=0
S=0
while S<N:
    K=K+1
    S=S+K
print("Наименьшее число K", K)
print("Сумма чисел", S)

print("Задание 9")
P=float(input("Введите процент увеличения вклада \n"))
S=1000
K=0
while S<=1100:
    S=S+S*P/100
    K=K+1
print("Количество месяцев", K)
print("Итоговый размер вклада", round(S, 2))

print("Задание 10")
A=int(input("Введите целое число A \n"))
B=int(input("Введите целое число B \n"))
while B!=0:
    R=A%B
    A=B
    B=R
print("Наибольший общий делитель", A)

