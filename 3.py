# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

class Tomato:
    states = {0: 'first state',
              1: 'second state',
              2: 'third state'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()
        # if self._state == self.states[0]:
        #     self._state = self.states[1]
        #     return self._state
        # elif self._state == self.states[1]:
        #     self._state = self.states[2]
        #     return self._state

    def is_ripe(self):
        if self._state == 3:
            return 'Созрел!'
        else:
            return 'Ещё не созрел!'

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} in {Tomato.states[self._state]}')


# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая

class TomatoBush:

    def __init__(self, count_tomato):
        # super().__init__(index=self._index)
        # self.count_tomato = count_tomato
        self.tomatoes = [Tomato(index) for index in range(1, count_tomato)]
        # i = 0
        # while i != count_tomato:
        #     self.tomatoes.append(self._state)
        #     i += 1

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
        # for i in self.tomatoes:
        #     i.is_ripe()
        #     # if i == self.states['third']:
        #     #     return True
        #     # else:
        #     #     return False

    def give_away_all(self):
        self.tomatoes = []


# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает.')
        self._plant.grow_all()
        print('Садочник закончил работу.')

    def harvest(self):
        print('Сбор урожая!')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            return 'Урожай собран'
        else:
            return 'Помидоры ещё не созрели!'

    @staticmethod
    def knowledge_base():
        return 'Справка по садоводству.'


Gardener.knowledge_base()
tomato_bash = TomatoBush(6)
gardener = Gardener('Tom', tomato_bash)
gardener.work()
print(gardener.harvest())
gardener.work()
gardener.work()
print(gardener.harvest())
