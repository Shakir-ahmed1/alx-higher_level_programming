#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        a = fct(*args)
        return (a)
    except Exception as ex:
        print("Exception: {}".format(str(ex)))
        return None
