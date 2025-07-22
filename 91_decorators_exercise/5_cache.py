def cache(func):
    log = {}
    def wrapper(*args, **kwargs):
        log[args[0]] = func(*args, **kwargs)
        result = func(*args, **kwargs)
        wrapper.log = log
        return result
    return wrapper
