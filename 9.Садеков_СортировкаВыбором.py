# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Задание 9. Сортировка выбором
"""

print("Задание 3")

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i], arr[min_idx]=arr[min_idx], arr[i]

arr=list(map(int, input("Введите элементы массива через пробел \n").split()))
selection_sort(arr)
print("Отсортированный массив", arr)

