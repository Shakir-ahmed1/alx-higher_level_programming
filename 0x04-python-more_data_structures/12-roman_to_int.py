#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    temp = ''
    result = 0
    for rome in roman_string:
        temp += rome
        if len(temp) == 2 and roman_num[temp[0]] < roman_num[temp[1]]:
            result += roman_num[temp[1]] - roman_num[temp[0]]
            temp = ''
        elif len(temp) == 4:
            for a in temp:
                result += roman_num[a]
            temp = ''
    if temp:
        for a in temp:
                result += roman_num[a]
    return result
