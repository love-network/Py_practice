#!/usr/bin/env python

def fib(times):
    if times < 1:
        print("Please input a valid value.")
        return None
    result = [0]
    if times >= 2:
        result.append(1)
        counter = 0
        if times > 2:
            while counter < (times - 2):
                result.append(result[-1] + result[-2])
                counter += 1
    return result

times = int(raw_input("Please enter the number of elements: "))
fib_result = fib(times)
print("The result list is:" + "\n" + str(fib_result))
