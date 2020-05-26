from functools import wraps
from time import sleep


def delay(sec):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f'Waiting {sec}s before running {fn.__name__}')
            sleep(sec)
            return fn(*args, **kwargs)
        return wrapper
    return decorator
