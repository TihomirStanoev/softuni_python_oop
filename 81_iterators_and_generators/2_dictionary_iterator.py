class dictionary_iter:
    def __init__(self, dictionary):
        self.dict_list = (el for el in dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.dict_list)


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)