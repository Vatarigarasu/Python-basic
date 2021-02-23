from abc import ABC, abstractmethod


class Clothes(ABC):
    total_material = 0

    @abstractmethod
    def material_needed(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V
        Clothes.total_material += self.material_needed

    @property
    def material_needed(self):
        return self.V/6.5+0.5


class Suit(Clothes):
    def __init__(self, H):
        self.H = H
        Clothes.total_material += self.material_needed

    @property
    def material_needed(self):
        return self.H*2 + 0.3


a = Coat(10)
b = Suit(10)
c = Coat(50)
d = Suit(8)

print(f'Общее колличество материалов требуемое для пошива одежды: {Clothes.total_material:.2f}')
