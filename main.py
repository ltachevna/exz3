# def bank(karta):
#     print(str(karta).replace(str(karta)[:12], '*' * 12))


# def palindrome(a):
#     if a == a[::-1]:
#         return True
#     else:
#         return False
from os import name

class Tomato:
    index = None
    states = {0: "Рост", 1: "Цветение", 2: "Формирование", 3: "Созревание"}

    def init(self, index, states=None):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            print("Созрел")
        else:
            print("Томат еще не созрел")

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 3:
            return True
        return False


class TomatoBush:

    def init(self, count):
        self.tomatoes = [Tomato(index) for index in range(0, count -1)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])



    def give_away_all(self):
        self.tomatoes = []



class Gardener:

    def init(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник начал работу')
        self._plant.grow_all()
        print('Садовник закончилл работу')

    def harvest(self):
        print('Садовник собирает урожай')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Садовник собрал урожай')
        else:
            print('Слишком рано! Ваше растение зеленое и незрелое.')

    @staticmethod
    def knowledge_base():
        print("В идеале врем сбора урожая помидоров должно наступить когда плод зрелый и зелёный")


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Алина', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()