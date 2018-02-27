#!/usr/bin/env python3

def safe_float(obj):
    try:
        retval = float(obj)
    except: #ValueError, e:
        retval = "error happens"
    else:
        retval = "no exceptions caught\n"
    return retval

def main():
    obj = input("please enter a float number: ")
    val = safe_float(obj)
    print(val)

if __name__ == "__main__":
    main()
