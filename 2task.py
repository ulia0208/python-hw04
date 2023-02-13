# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

n=int(input('Количество кустов черники - '))

berries_list=[]
three_berries=[]

for i in range(n):
    berries_list.append(int(input()))

print(berries_list)


berries=0

if n<4:
    for i in range(n):
        berries+=berries_list[i]

else:
    for i in range(n):
        if i==n-1:
            three_berries.append(berries_list[i]+berries_list[0]+berries_list[1])
        elif i==n-2:
            three_berries.append(berries_list[i]+berries_list[i+1]+berries_list[0])
        elif i<n-2:
            three_berries.append(berries_list[i]+berries_list[i+1]+berries_list[i+2])


print(berries)


print(three_berries)

max=0
for i in range(len(three_berries)):
    if three_berries[i]>max:
        max=three_berries[i]

print(max)