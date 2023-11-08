#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    num = 0
    for d in my_list:
        score += d[0] * d[1]
        num += d[1]
        return (score / num)
