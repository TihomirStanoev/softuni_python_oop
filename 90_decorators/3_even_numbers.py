def even_numbers(func):
    def wrapper(*args, **kwargs):
        result = [x for x in func(*args, **kwargs) if x % 2 == 0]
        return result
    return wrapper