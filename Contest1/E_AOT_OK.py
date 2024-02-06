##E. Среднее из трёх
##Даны три числа: a, b, c. Найти среднее из них.
##
##Формат ввода
##Строка с тремя числами a, b, c.
##
##Формат вывода
##Среднее по значению из введенных чисел.

numbers = input().split(" ")
for j in range(2):
    for i in range(2):
        if int(numbers[i]) > int(numbers[i + 1]):
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(numbers[1])
