def vowel_filter(func):
    def wrapper(*args):
        result = [letter for letter in func(*args) if letter in 'aeiou']
        return result
    return wrapper