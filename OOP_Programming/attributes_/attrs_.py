# Ask for forgiveness rather than permission.

class Vector:
    def __init__(self, **components):
        protected_components = {f'_{key}': value for key, value in components.items()}
        self.__dict__.update(protected_components)

    def __getattr__(self, name):
        protected_name = f'_{name}'
        if protected_name not in self.__dict__:
            raise AttributeError(f'{self!r} object has no attribute {name!r}')
        return getattr(self, protected_name)

    def __setattr__(self, name, value):
        raise AttributeError(f"Can`t set attribute {name!r}")

    def __repr__(self):
        return f'{type(self).__name__}({", ".join(
            f'{key[1:]}={value}' for key, value in self.__dict__.items()
        )})'


v1 = Vector(x=1, y=2)
v2 = Vector(p=3, q=4)
# print(v1.__dict__)
# print(v2.__dict__)

# print(v2.p)
# print(v1.x)
# print(v1.dupa)

v1.x = 42
print(v1.__dict__)
print(v1.x)

# # print(type(v))
# v.__dict__['z'] = 100
# del v.__dict__['x']
# print(v.z)
# print(getattr(v, 'z'))
# print(hasattr(v, 'z'))
# delattr(v, 'z')
# print(v.__dict__)
