from memory_profiler import profile


class Worker():
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    @profile
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    @profile
    def get_total_income(self):
        print(f'Total income is {self._income["wage"] + self._income["bonus"]}')


class Worker_opt:
    __slots__ = ['name', 'surname', 'position', 'income']

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position_opt(Worker_opt):
    @profile
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    @profile
    def get_total_income(self):
        print(f'Total income is {self.income["wage"] + self.income["bonus"]}')


first_worker_opt, snd_worker_opt = Position_opt('Max', 'Loren', 'manager', {'wage': 1000, 'bonus': 500}), \
                                   Position_opt('Alex', 'Stevenson', 'Driver', {'wage': 1200, 'bonus': 100})
first_worker_opt.get_full_name()
first_worker_opt.get_total_income()
snd_worker_opt.get_full_name()
snd_worker_opt.get_total_income()

first_worker, snd_worker = Position('Max', 'Loren', 'manager', {'wage': 1000, 'bonus': 500}), \
                           Position('Alex', 'Stevenson', 'Driver', {'wage': 1200, 'bonus': 100})

first_worker.get_full_name()
first_worker.get_total_income()
snd_worker.get_full_name()
snd_worker.get_total_income()


# Оптимизация за счет использования слотов