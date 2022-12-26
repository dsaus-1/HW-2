'''
1. Реализуйте алгоритм, который принимает массив и перемещает нули в конец,
сохраняя порядок остальных элементов
'''

def sort_zero(lst):
    answer = lst.copy()
    count_1 = 0
    count_2 = 1
    while count_2 <= len(answer)-count_2:
        if answer[count_1] == 0:
            answer.pop(count_1)
            answer.append(0)
            count_2 += 1
        else:
            count_1 += 1
    return answer


assert sort_zero([0, 2, 3, 1, 0, 0, 1, 3]) == [2, 3, 1, 1, 3, 0, 0, 0]


'''
2. Посчитайте сумму н-го ряда пирамиды нечетных чисел (начало с 1)
    
#   1 
#  3 5 
# 7 9 11
# 13 15 17 19
#21 23 25 27 29
#...
'''

def sum_odd_numbers(row):
    number = 0
    answer = []
    for number_digits in range(1, row+1):
        number += number_digits

    for s in range(1, number * 2, 2):
        answer.append(s)
    return sum(answer[-row::])


    # if row == 1:
    #     return 1
    # start = sum_odd_numbers(row-1)
    # for i in range(start, start + row*2, 2):
    #     print(i)
    # return sum(range(start, start + row*2, 2))



print(sum_odd_numbers(5))
