class Zoo:
    def __init__(self, name:str, budget:int, animal_capacity:int, workers_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []


    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return 'Not enough space for animal'
        if self.__budget < price:
            return 'Not enough budget'

        self.animals.append(animal)
        self.__budget -= price

        return f'{animal.name} the {type(animal).__name__} added to the zoo'


    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)

        return f'{worker.name} the {type(worker).__name__} hired successfully'


    def fire_worker(self, worker_name):
        exist_worker = next((w for w in self.workers if w.name == worker_name), None)

        if exist_worker:
            self.workers.remove(exist_worker)
            return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'


    def pay_workers(self):
        salary_amount = sum(worker.salary for worker in self.workers)
        if self.__budget < salary_amount:
            return 'You have no budget to pay your workers. They are unhappy'

        self.__budget -= salary_amount
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'


    def tend_animals(self):
        needed_budget = sum(animal.money_for_care for animal in self.animals)

        if self.__budget < needed_budget:
            return 'You have no budget to tend the animals. They are unhappy.'

        self.__budget -= needed_budget
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'


    def profit(self, amount):
        self.__budget += amount


    @staticmethod
    def __result(object_list, status):
        result = [f'You have {len(object_list)} {status}']
        result_dict = {}

        for object_ in object_list:
            object_type = type(object_).__name__
            if object_type in result_dict:
                result_dict[object_type].append(f'{object_!r}')
            else:
                result_dict[object_type] = [f'{object_!r}']

        for object_type, object_ in result_dict.items():
            result.append(f'----- {len(object_)} {object_type}s:')
            for obj in object_:
                result.append(obj)

        return '\n'.join(result)

    def animals_status(self):
        return self.__result(self.animals, 'animals')

    def workers_status(self):
        return self.__result(self.workers, 'workers')



    # TODO: Make this two methods in one.
    # def animals_status(self):
    #     result = [f'You have {len(self.animals)} animals']
    #     total_animals = {'Lion':[], 'Tiger': [], 'Cheetah': []}
    #
    #     for animal in self.animals:
    #         animal_type = type(animal).__name__
    #         total_animals[animal_type].append(f'{animal!r}')
    #
    #     for animal_type, animals in total_animals.items():
    #         result.append(f'----- {len(animals)} {animal_type}s:')
    #         for animal in animals:
    #             result.append(animal)
    #
    #     return '\n'.join(result)
    #
    # def workers_status(self):
    #     result = [f'You have {len(self.workers)} workers']
    #     total_workers = {'Keeper':[], 'Caretaker': [], 'Vet': []}
    #
    #     for worker in self.workers:
    #         worker_type = type(worker).__name__
    #         total_workers[worker_type].append(f'{worker!r}')
    #
    #     for worker_type, workers in total_workers.items():
    #         result.append(f'----- {len(workers)} {worker_type}s:')
    #         for worker in workers:
    #             result.append(worker)
    #
    #     return '\n'.join(result)
