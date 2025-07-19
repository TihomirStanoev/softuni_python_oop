class vowels:
    VOWELS = 'aeiuyo'
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.index < len(self.string):
            self.index += 1
            current_char = self.string[self.index - 1]
            if current_char.lower() in self.VOWELS:
                return current_char
        raise StopIteration



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)