"""Написать программу, которая:
- Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине, заполненную значениями из списка **[-3, -5, -2, -12, 0, 15, 4, 7, 2]**
- Выводит данную матрицу в форматированном виде.
- Выводит сумму всех элементов кратных 3"""
import random #Подключение модуля random

list=[-3, -5, -2, -12, 0, 15, 4, 7, 2] #Список чисел для заполнения матрицы
h=int(input("Введите кол-во строк вашей матрицы(от 4 до 8): ")) #Ввод кол-ва строк матрицы с клавиатуры
w=int(input("Введите кол-во столбцов вашей матрицы(от 4 до 8): ")) #Ввод кол-ва столбцов матрицы с клавиатуры

matrix=[] #Создание пустой матрицы

for i in range(h): #Цикл for для заполнения строк
    line = [] #Создание пустого списка для строк
    for j in range(w): #Цикл for для заполнения столбцов
        line.append(random.choice(list)) #Добавление рандомного элемента из списка list в список line
    matrix.append(line) #Добавление списка line в матрицу
    
print("Ваша матрица: ") #Вывод текста на консоль
for line in matrix: #Цикл for для вывода элементов матрицы на консоль
    for i in line: #Цикл for для вывода элементов списка line на консоль
        print(i, end="  ") #Вывод элемента на консоль с разделением пробелом
    print() #Переход на новую строку
    
sum=0 #Создание переменной для суммы чисел кратных трем

for line in matrix: #Цикл for для перебора элементов матрицы
    for i in line: #Цикл for для перебора элементов списка line
        if i%3==0 and i!=0: #Цикл if для проверки кратности трем и неравества элемента нулю
            sum+=i #Прибавление элемента к сумме при истинности условия
print("Сумма чисел кратных трем в вашей матрице: ", sum) #Вывод на консоль суммы элементов кратных трем
