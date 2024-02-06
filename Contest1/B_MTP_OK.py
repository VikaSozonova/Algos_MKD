##B. Больше предыдущего
##На уроке информатики Васе рассказали про сортировку натуральных чисел и он
##решил придумать метрику, по которой он мог бы судить, насколько
##последовательность отсортирована. Для этого он решил считать, сколько
##элементов последовательности больше, чем предыдущий элемент. Напишите
##программу, решающую эту задачу.
##
##Формат ввода
##Вводится последовательность целых чисел, оканчивающаяся нулем (сам 0 в
##последовательность не входит).
##
##Формат вывода
##Программа должна вывести сколько элементов введенной последовательности
##больше предыдущего элемента.

prev = int(input())
cur = int(input())
k = 0
while prev != 0 and cur != 0:
    if prev < cur:
        k += 1
    prev = cur
    cur = int(input())
print(k)