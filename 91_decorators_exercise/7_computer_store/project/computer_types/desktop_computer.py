from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    @property
    def available_ram(self):
        return [2 ** gb for gb in range(1,8)]

    @property
    def processors(self):
        return {'AMD Ryzen 7 5700G': 500,
                  'Intel Core i5-12600K': 600,
                  'Apple M1 Max': 1800}

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processors:
            raise ValueError(f'{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!')
        if ram not in self.available_ram:
            raise ValueError(f'{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!')

        super().configure_computer(processor, ram)

        return f'Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$.'