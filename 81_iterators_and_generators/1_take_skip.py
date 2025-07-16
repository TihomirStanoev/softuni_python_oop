class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0



    def __iter__(self):
        return self

    def __next__(self):
        if self.number >= self.count:
            raise StopIteration
        result = self.number * self.step
        self.number += 1
        return result



numbers = take_skip(10, 5)
for number in numbers:
    print(number)