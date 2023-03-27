#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for ls in my_list:
            if counter != x:
                counter += 1
                print(ls, end="")
            else:
                print()
                return counter
        print()
        return counter
    except Exception:
        raise
