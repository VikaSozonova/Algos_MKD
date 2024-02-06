##C. Холмы
##Локацией некоторой игры является вереница холмов, по которой ездит
##автомобиль. Каждый холм характеризуется высотой в метрах. Будем считать холм
##локальной вершиной, если его высота строго больше, чем у предыдущего и
##следующего холма в веренице. При этом первый и последний холмы локации не
##могут быть локальными вершинами. Необходимо найти минимальное число холмов,
##находящееся между двумя локальными вершинами локации. Если на локации
##невозможно найти две локальные вершины, выведите число -1.
##
##Формат ввода
##На вход программа получает последовательность натуральных чисел - высоты
##холмов, оканчивающаяся нулем (сам 0 в последовательность не входит).
##
##Формат вывода
##Программа должна вывести минимальное число холмов, находящееся между двумя
##локальными вершинами.

curent = int(input())
hills = []
while curent != 0:
    hills.append(curent)
    curent = int(input())
max_hills = []
min_distance = len(hills)
index_first = -1
index_second = -1
for i in range(len(hills) - 2):
    if (hills[i] < hills[i + 1]) and (hills[i + 1] > hills[i + 2]):
        index_first = index_second
        index_second = i + 1
        if index_second - index_first - 1 < min_distance:
            min_distance = index_second - index_first - 1
        i += 1
if index_first != -1 and index_second != -1:
    print(min_distance)
else:
    print(-1)
        