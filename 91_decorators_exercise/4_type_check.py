def type_check(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(True if isinstance(x, arg) else False for x in args):
                return func(*args, **kwargs)
            return 'Bad Type'
        return wrapper
    return decorator
