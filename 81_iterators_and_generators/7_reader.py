def read_next(*args):
    for i in args:
        for x in i:
            yield x


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)