#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    if len(str) <= n or n < 0:
        return str
    for s in range(len(str)):
        if s != n:
            nstr = nstr + str[s]
    return nstr

        
print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
