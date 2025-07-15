roman_to_arabic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Integer:
    def __init__(self, value:int):
        self.value = value


    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        number = 0
        for index in range(len(value)-1):
            if roman_to_arabic[value[index + 1]] > roman_to_arabic[value[index]]:
                number -= roman_to_arabic[value[index]]
            else:
                number += roman_to_arabic[value[index]]
        else:
            number += roman_to_arabic[value[-1]]

        return cls(number)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"



first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))