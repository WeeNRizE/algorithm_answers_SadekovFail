# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Задание 7. Сортировка пузырьком
"""

print("Задание 1")

def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swapped=True
        if not swapped:
            break

arr=list(map(int, input("Введите элементы массива через пробел \n").split()))
bubble_sort(arr)
print("Отсортированный массив", arr)


