def even_parameters(func):
    def wrapper(*args):
        if all(True if isinstance(x, int) and x % 2 == 0 else False for x in args):
            return func(*args)
        return 'Please use only even numbers!'
    return wrapper



@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))