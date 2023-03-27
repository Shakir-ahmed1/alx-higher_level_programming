#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for ls in range(x):
            if isinstance(my_list[ls], int):
                print("{:d}".format(my_list[ls]), end="")
                count += 1
        print()
        return count
    except Exception:
        raise
