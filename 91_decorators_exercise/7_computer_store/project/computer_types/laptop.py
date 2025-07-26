from project.computer_types.computer import Computer

class Laptop(Computer):
    @property
    def available_ram(self):
        return [2 ** gb for gb in range(1,7)]

    @property
    def processors(self):
        return {'AMD Ryzen 9 5950X': 900,
                  'Intel Core i9-11900H': 1050,
                  'Apple M1 Pro': 1200}

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processors:
            raise ValueError(f'{processor} is not compatible with laptop {self.manufacturer} {self.model}!')
        if ram not in self.available_ram:
            raise ValueError(f'{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!')

        super().configure_computer(processor, ram)
        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'
