from collections import deque

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = deque(sequence)
        self.number = number


    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        item = self.sequence[0]
        self.sequence.rotate(-1)
        self.number -= 1

        return item

#
# class sequence_repeat:
#     def __init__(self, sequence, number):
#         self.sequence = sequence
#         self.number = number
#         self.produced_count = 0
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.number <= 0:
#             raise StopIteration
#         index = self.produced_count % len(self.sequence)
#         self.number -= 1
#         self.produced_count += 1
#
#         return self.sequence[index]



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')