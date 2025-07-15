class Calculator:
    @staticmethod
    def add(*args, num_sum = 0, inx = 0):
        num_sum += args[inx]
        if inx == len(args) - 1:
            return num_sum
        return Calculator.add(*args, num_sum=num_sum, inx=inx + 1)

    @staticmethod
    def multiply(*args, mult = 1, inx = 0):
        mult *= args[inx]
        if inx == len(args)-1:
            return mult
        return Calculator.multiply(*args, mult=mult, inx= inx + 1)

    @staticmethod
    def divide(*args, div = 1, inx = 0):
        if len(args) == inx:
            return div
        elif inx == 0:
            div = args[inx]
        elif args[inx] == 0:
            div = 1
        else:
            div /= args[inx]
        return Calculator.divide(*args, div=div, inx= inx + 1)

    @staticmethod
    def subtract(*args, sub = 0, inx = 0):
        if inx == len(args):
            return sub
        elif inx == 0:
            sub = args[inx]
        else:
            sub -= args[inx]

        return Calculator.subtract(*args, sub=sub, inx=inx + 1)



print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))