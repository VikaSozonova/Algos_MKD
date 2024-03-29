##D. Симметрия
##Петя и Вася играют в игру со следующими правилами: Петя называет
##четырехзначное число, а Вася должен быстро понять, симметричное оно или нет.
##Если число симметричное, Вася говорит: "1", иначе любое другое число, которое
##придет ему в голову. Иногда Петя забывает, что числа должны быть
##четырехзначными, и называет число, в котором меньше четырех знаков. В таком
##случае Вася считает, что десятичная запись числа слева дополняется
##незначащими нулями.
##
##Формат ввода
##Вводится не более чем четырехзначное целое число.
##
##Формат вывода
##Программа должна вывести 1, если число симметричное, а иначе любое другое
##целое число.

number = input()[-4:]
if int(number) < 1000:
    number = "0" + number
if number == number[::-1]:
    print(1)
else:
    print(int(number[1:3]) + 2)
