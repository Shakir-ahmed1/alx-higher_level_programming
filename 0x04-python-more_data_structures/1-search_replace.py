#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for ls in my_list:
        if ls == search:
            result.append(replace)
        else:
            result.append(ls)
    return result
