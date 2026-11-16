# -*- coding: utf-8 -*-
"""
@author: Садеков Фаиль Группа 243-321

Задание 11. Работа с деревьями
"""

print("Задание 11")

class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def insert(root, value):
    if root is None:
        return Node(value)
    if value<root.value:
        root.left=insert(root.left, value)
    else:
        root.right=insert(root.right, value)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

A=list(map(int, input("Введите элементы дерева через пробел \n").split()))
tree=None
for i in A:
    tree=insert(tree, i)

print("Обход дерева в порядке возрастания:")
inorder_traversal(tree)
print()


