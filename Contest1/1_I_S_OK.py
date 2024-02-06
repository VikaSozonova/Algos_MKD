##I. Прожектора
##На дискотеке в ряд стоят три прожектора, которые поочерёдно светят в
##следующем порядке: левый, средний, правый, средний, левый, средний, правый,
##средний и т.д. (слева направо, затем налево, опять направо, ...). Каждый
##прожектор горит в течение одной секунды.
##
##Известно, что лампа левого прожектора имеет ресурс A секунд горения,
##среднего — B секунд, правого — C секунд. Определите, сколько времени сможет
##продолжаться этот процесс горения прожекторов.
##
##Формат ввода
##Программа получает на вход три целых неотрицательных числа A, B, C — время
##горения левого, среднего, правого прожектора.
##
##Формат вывода
##Программа должна вывести одно целое число.

spotlights = [int(input()) for i in range(3)]
n = min(spotlights[0], spotlights[1] // 2, spotlights[2])
spotlights[0] -= n
spotlights[1] -= 2 * n
spotlights[2] -= n
k = 4 * n
curent = spotlights[0]
curent_index = 0
to_right = True
while curent != 0:
    k += 1
    spotlights[curent_index] -= 1
    if to_right:
        curent_index += 1
    else:
        curent_index -= 1
    curent = spotlights[curent_index]
    if curent_index == 2:
        to_right = False
    elif curent_index == 0:
        to_right = True
print(k)
        
