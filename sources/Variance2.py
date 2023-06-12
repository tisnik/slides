from typing import Sequence


class Fruit:
    pass


class Orange(Fruit):
    def __repr__(self):
        return "Orange"


class Apple(Fruit):
    def __repr__(self):
        return "Apple"


def printContent(punnet : Sequence[Fruit]):
    for Fruit in punnet:
        print(Fruit)


punnet : Sequence[Orange] = [Orange(), Orange(), Orange()]

printContent(punnet)
