from time import time, sleep


def timeit_with_sleep(sleep_time):
    def time_decorator(func):
        def wrapper(*args, **kwargs):
            start = time()
            sleep(sleep_time)
            ret = func(*args, **kwargs)
            print(f'Function execution took: {time() - start} seconds')
            return ret
        return wrapper
    return time_decorator


@timeit_with_sleep(1)
def iterate(arg):
    for _ in range(100000):
        pass
    print(arg)


iterate('something')



