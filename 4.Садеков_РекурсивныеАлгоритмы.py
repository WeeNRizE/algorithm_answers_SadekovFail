# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Лабораторная работа №4 Рекурсивные алгоритмы
"""

print("Задание 1")
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

n=int(input("Введите неотрицательное число n \n"))
print("Факториал числа", factorial(n))


print("Задание 2")
"""Данный код написан считая, что 0 это нулевое число Фибоначчи. комменариями рядом со строками написаны строки, на которые надо изменить код, чтобы 0 считался 1 элементом"""
def fibonacci(n):
    """if n==1:"""
    if n==0:
        return 0
    """if n==2:"""
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Введите номер числа Фибоначчи n \n"))
print("Число Фибоначчи", fibonacci(n))


print("Задание 3")
def power(x, n):
    if n==0:
        return 1
    if n<0:
        return 1/power(x, -n)
    return x*power(x, n-1)

x=float(input("Введите число x \n"))
n=int(input("Введите степень n \n"))
print("Результат возведения в степень", power(x, n))


print("Задание 4")
def palindrome(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return palindrome(s[1:-1])

s=input("Введите строку \n")
s=s.lower().replace(" ", "")
if palindrome(s):
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")


print("Задание 5")
def binary_search(a, x, left, right):
    if left>right:
        return -1
    mid=(left+right)//2
    if a[mid]==x:
        return mid
    if a[mid]>x:
        return binary_search(a, x, left, mid-1)
    return binary_search(a, x, mid+1, right)

a=list(map(int, input("Введите отсортированные числа через пробел \n").split()))
x=int(input("Введите искомое число \n"))
result=binary_search(a, x, 0, len(a)-1)
if result==-1:
    print("Элемент не найден")
else:
    print("Элемент найден на позиции", result+1)


print("Задание 6")
def reverse_words(s):
    words=s.split(maxsplit=1)
    if len(words)==0:
        return ""
    if len(words)==1:
        return words[0]
    return reverse_words(words[1])+" "+words[0]

s=input("Введите строку \n")
print("Обратный порядок слов:", reverse_words(s))


print("Задание 7")
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def prime_sum(n):
    if n==0:
        return []
    for i in range(n, 1, -1):
        if is_prime(i):
            result=prime_sum(n-i)
            if result is not None:
                return [i]+result
    return None
n=int(input("Введите целое число не меньше 2 \n"))
result=prime_sum(n)
print("Разложение на простые числа:", " + ".join(map(str, result)))


print("Задание 8")
def count_digits(n):
    if n<10:
        return 1
    return 1+count_digits(n//10)

n=int(input("Введите целое число \n"))
n=abs(n)
print("Количество цифр в числе", count_digits(n))


print("Задание 9")
def hanoi(n, source, target, auxiliary):
    if n==1:
        print("Переместить диск 1 с", source, "на", target)
        return
    hanoi(n-1, source, auxiliary, target)
    print("Переместить диск", n, "с", source, "на", target)
    hanoi(n-1, auxiliary, target, source)

n=int(input("Введите количество дисков \n"))
hanoi(n, "A", "C", "B")


