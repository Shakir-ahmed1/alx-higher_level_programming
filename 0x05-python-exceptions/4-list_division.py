#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    temp = 0
    try:
        pass
    except Exception:
        pass
    finally:
        pass

    for i in range(list_length):
        try:
            temp = my_list_1[i] / my_list_2[i]
        except TypeError:
            temp = 0
            print("wrong type")
        except ZeroDivisionError:
            temp = 0
            print("division by 0")
        except IndexError:
            temp = 0
            print("out of range")
        finally:
            result.append(temp)
    return result
