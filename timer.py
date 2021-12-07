import functools
import time

def timer(function):
    @functools.wraps(function)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        _ = function(*args, **kwargs)
        finish = time.perf_counter()
        print(f"Completed in {finish - start:0.5f} secs")
        return _
    return wrapper_timer