from typing import List


class Fruit:
    pass


class Orange(Fruit):
    def __repr__(self):
        return "Orange"


class Apple(Fruit):
    def __repr__(self):
        return "Apple"


def printContent(punnet : List[Fruit]):
    for Fruit in punnet:
        print(Fruit)


punnet : List[Orange] = [Orange(), Apple(), Orange()]

printContent(punnet)
