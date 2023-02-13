# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n=int(input('Введите количество элементов первого множества '))



my_collection1=set()
print('Первый набор чисел ')
for i in range(n):
    my_collection1.add(int(input()))



m=int(input('Введите количество элементов второго множества '))

my_collection2=set()
print('Второй набор чисел ')
for i in range( m):
    my_collection2.add(int(input()))

print(my_collection1)
print(my_collection2)


my_collection=sorted(my_collection1.intersection(my_collection2))





print(my_collection)