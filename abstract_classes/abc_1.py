class SwordMeta(type):

    def __subclasscheck__(cls, subclass):
        return True


class Sword(metaclass=SwordMeta):
    """Abstract Base Class"""


class BroadSword:
    def swipe(self):
        print('Swoosh!', type(self).__name__)

    def sharpe(self):
        print('Shrink!', type(self).__name__)


class SamuraiSword:
    def swipe(self):
        print('Slice!', type(self).__name__)

    def sharpe(self):
        print('Shrink!', type(self).__name__)