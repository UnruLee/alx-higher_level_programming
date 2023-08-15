#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = my_list.copy()

    for x in range(0, len(list_result)):
        if x % 2 == 0:
            list_result[x] = True
        else:
            list_result[x] = False

    return list_result
