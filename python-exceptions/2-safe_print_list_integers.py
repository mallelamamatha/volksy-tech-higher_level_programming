#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i])
                    y += 1
        except (ValueError, IndexError):
            continue
        except (KeyError):
            raise
    print()
    return y
