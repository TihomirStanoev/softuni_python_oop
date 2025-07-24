def multiply(param):
    def decorator(func):
        def wrapper(x):
            return func(x) * param
        return wrapper
    return decorator