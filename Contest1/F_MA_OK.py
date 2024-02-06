##F. Максимальная площадь
##Даны N прямоугольников. Найти максмальную площадь среди данных фигур.
##
##Формат ввода
##Сначала на вход подается число N - количество прямоугольников.
##Затем на вход подается N строк с четырьмя числами - координатами
##противоположных углов прямоугольника (x1, y1, x2, y2).
##
##Формат вывода
##Одно число - максимальная площадь из введенных фигур.

n = int(input())
max_area = 0
for i in range(n):
    coordinates = input().split(" ")
    length = int(coordinates[2]) - int(coordinates[0])
    if length < 0:
        length = -length
    hight = int(coordinates[3]) - int(coordinates[1])
    if hight < 0:
        hight = -hight
    curent_area = length * hight
    max_area = max(curent_area, max_area)
print(max_area)
