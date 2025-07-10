class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


    def __add__(self, other):
        return Person(self.name, other.surname)

class Group:
    def __init__(self, name:str, people: list[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people) if self.people else 0

    def __add__(self, other):
        name = f'{self.name} {other.name}'
        people = self.people + other.people
        return Group(name, people)

    def __repr__(self):
        return f'Group {self.name} with members {", ".join(str(p) for p in self.people)}'

    def __iter__(self):
        for index, person_obj in enumerate(self.people):
            yield f'Person {index}: {person_obj}'

    def __getitem__(self, item):
        index = lambda i: range(len(self.people))[i]
        return f'Person {index(item)}: {self.people[item]}'



p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[-1])
