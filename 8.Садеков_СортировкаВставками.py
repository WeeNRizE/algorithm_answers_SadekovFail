# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Задание 8. Сортировка вставками
"""

print("Задание 2")

def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

arr=list(map(int, input("Введите элементы массива через пробел \n").split()))
insertion_sort(arr)
print("Отсортированный массив", arr)


