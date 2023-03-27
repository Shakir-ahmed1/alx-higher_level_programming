#!/usr/bin/python
def raise_exception_msg(message=""):
    try:
        raise Exception
    except Exception:
        print(message)

