#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or isinstance(roman_string, str):
        return 0
    roman_num = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    temp = ''
    result = 0
    skip = []
    i = -1
    for a in range(len(roman_string) - 1):
        if roman_num[roman_string[a]] < roman_num[roman_string[a+1]]:
            skip.append(a)
    for rome in roman_string:
        i += 1
        if i in skip:
            for a in temp:
                result += roman_num[a]
            temp = rome
            continue
        temp += rome
        if len(temp) == 2 and roman_num[temp[0]] < roman_num[temp[1]]:
            result += roman_num[temp[1]] - roman_num[temp[0]]
            temp = ''
    if temp:
        for a in temp:
            result += roman_num[a]
    return result
