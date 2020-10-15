from functools import wraps
from datetime import datetime
# from memory_profiler import profile
from sys import getsizeof

def time_memory(func):
    """Returns the execution time and and memory usage of a function. """
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        data = func(*args, **kwargs)
        t2 = datetime.now()
        total_time = 'function execution time: {}'.format(t2 - t1)

        print("function size: ", getsizeof(data))
        print("function return type: ", type(data))
        print(total_time)
        return data
    return wrapper
