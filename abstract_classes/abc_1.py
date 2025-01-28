from abc import ABCMeta


class SwordMeta(type):

    def __instancecheck__(cls, instance):
        return issubclass(type(instance), cls)

    def __subclasscheck__(cls, subclass):
        if (
            hasattr(subclass, 'swipe') and callable(subclass.swipe)
            and
            hasattr(subclass, 'sharpen') and callable(subclass.sharpen)
        ):
            return True
        return super().__subclasscheck__(subclass)


class Sword(metaclass=ABCMeta):
    """Abstract Base Class"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                (
                        hasattr(subclass, 'swipe') and callable(subclass.swipe)
                        and
                        hasattr(subclass, 'sharpen') and callable(subclass.sharpen)
                )
                or
                NotImplemented
        )

    def thrust(self):
        print('Thrust!', type(self).__name__)


class BroadSword:
    def swipe(self):
        print('Swoosh!', type(self).__name__)

    def sharpen(self):
        print('Shrink!', type(self).__name__)


class SamuraiSword:
    def swipe(self):
        print('Slice!', type(self).__name__)

    def sharpen(self):
        print('Shrink!', type(self).__name__)

class Rifle:
    def fire(self):
        print('Bang!!', type(self).__name__)

class Sabre(Sword):
    pass

@Sword.register
class LightSabre:
    def swipe(self):
        print('Ffffkrrrrshhzzzwooooom..woom..woom!', type(self).__name__)

samurai_sword = SamuraiSword()

sabre = Sabre()
print(issubclass(LightSabre, Sword))
print(isinstance(sabre, Sword))