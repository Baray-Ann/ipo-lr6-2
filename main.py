"""Написать программу, которая:
- Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине, заполненную значениями из списка **[-3, -5, -2, -12, 0, 15, 4, 7, 2]**
- Выводит данную матрицу в форматированном виде.
- Выводит сумму всех элементов кратных 3"""
import random
list=[-3, -5, -2, -12, 0, 15, 4, 7, 2]
h=int(input("Введите кол-во строк вашей матрицы(от 4 до 8): "))
w=int(input("Введите кол-во столбцов вашей матрицы(от 4 до 8): "))
matrix=[]
for i in range(h):
    line = []
    for j in range(w):
        line.append(random.choice(list))
    matrix.append(line)
print("Ваша матрица: ")
for line in matrix:
    for i in line:
        print(i, end="  ")
    print()
sum=0
for line in matrix:
    for i in line:
        if i%3==0 and i!=0:
            sum+=i
print("Сумма чисел кратных трем в вашей матрице: ", sum)