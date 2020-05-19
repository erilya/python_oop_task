from time import time
import math


def timing_function(some_function):
    """
    Outputs the time a function takes to execute.
    """
    def wrapper(*args, **kwargs):
        t1 = time()
        print("call %s:" % some_function.__name__)
        result = some_function(*args, **kwargs)
        print("Result:\n%s" % " ".join([str(x) for x in result]))
        t2 = time()
        print("Time it took to run the function: %.4f sec\n" % (t2 - t1))

    return wrapper


@timing_function
def simple_digit1(n):
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


@timing_function
def simple_digit2(n):
    result = []
    for i in range(2, n+1):
        for j in result:
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


@timing_function
def simple_digit3(n):

    result = []
    for i in range(2, n+1):
        if i > 10:
            if i % 2 == 0 or i % 10 == 5:
                continue
        for j in result:
            if j > int((math.sqrt(i)) + 1):
                result.append(i)
                break
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


n = 10000
simple_digit1(n)
simple_digit2(n)
simple_digit3(n)
