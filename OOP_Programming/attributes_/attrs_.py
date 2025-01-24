class Vector:
    def __init__(self, **components):
        self.__dict__.update(components)


    def __repr__(self):
        return f'{type(self).__name__}({", ".join(
            f'{key}={value}' for key, value in self.__dict__.items()
        )})'


v1 = Vector(x=1, y=2)
v2 = Vector(p=3, q=4)
print(v1.__dict__)
print(v2.__dict__)

print(v2.p)
print(v1)

# # print(type(v))
# v.__dict__['z'] = 100
# del v.__dict__['x']
# print(v.z)
# print(getattr(v, 'z'))
# print(hasattr(v, 'z'))
# delattr(v, 'z')
# print(v.__dict__)
