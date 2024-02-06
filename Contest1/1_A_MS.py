##A. Монотонная подпоследовательность
##Вася придумал новую метрику по которой он может делать выводы о том,
##насколько отсортирована последовательность натуральных чисел. Для этого он
##находит длину наибольшей монотонной подпоследовательности. Монотонной
##подпоследовательностью считается такой фрагмент последовательности, в
##котором все элементы располагаются либо в порядке возрастания, либо в
##порядке убывания. Напишите программу, вычисляющую эту метрику.
##
##Формат ввода
##Вводится последовательность целых чисел, оканчивающаяся нулем (сам 0 в
##последовательность не входит).
##
##Формат вывода
##Программа должна вывести длину максимальной монотонной подпоследовательности.

kb = 1
mkb = 0
km = 1
mkm = 0
prev = int(input())
if prev == 0:
    km = 0
    kb = 0
while prev != 0:
    cur = int(input())
    if cur != 0:
        if cur >= prev:
            kb += 1
            mkm = max(mkm, km)
        else:
            km = 1
        if cur <= prev:
            km += 1
            mkb = max(mkb, kb)
        else:
            kb = 1
    prev = cur

print(max(mkb, mkm))
