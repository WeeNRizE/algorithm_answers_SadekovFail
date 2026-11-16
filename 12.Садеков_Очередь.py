# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Задание 12. Очередь
"""

from collections import deque

print("Задание 12")
q=deque(map(int, input("Введите элементы очереди через пробел \n").split()))

while True:
    print("\n1. Добавить элемент")
    print("2. Извлечь элемент")
    print("3. Посмотреть первый элемент")
    print("4. Проверить пустоту очереди")
    print("5. Узнать размер очереди")
    print("6. Проверить наличие элемента")
    print("7. Очистить очередь")
    print("8. Вывести элементы очереди")
    print("0. Завершить работу")

    choice=int(input("Выберите действие \n"))

    if choice==0:
        break
    elif choice==1:
        x=int(input("Введите элемент \n"))
        q.append(x)
        print("Элемент добавлен")
    elif choice==2:
        if q:
            print("Извлеченный элемент", q.popleft())
        else:
            print("Очередь пуста")
    elif choice==3:
        if q:
            print("Первый элемент", q[0])
        else:
            print("Очередь пуста")
    elif choice==4:
        if not q:
            print("Очередь пуста")
        else:
            print("Очередь не пуста")
    elif choice==5:
        print("Размер очереди", len(q))
    elif choice==6:
        x=int(input("Введите искомый элемент \n"))
        if x in q:
            print("Элемент найден")
        else:
            print("Элемент не найден")
    elif choice==7:
        q.clear()
        print("Очередь очищена")
    elif choice==8:
        print("Элементы очереди", list(q))

