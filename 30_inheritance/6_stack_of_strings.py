class Stack:
    def __init__(self, *args):
        self.data = [self.checking_string(element) for element in args]

    @staticmethod
    def checking_string(element):
        if not isinstance(element, str):
            raise TypeError("Only str are allowed")
        return element

    def push(self, element):
        self.data.append(self.checking_string(element))

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not bool(self.data)

    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'
