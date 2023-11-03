#!/usr/bin/python3
def no_c(my_string):
    c_str = my_string.translate({ord[i]: None for i in 'cC'})
    return c_str
