from weakref import WeakKeyDictionary


class Positive:
    def __init__(self):
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._instance_data[instance]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"Value {value} is not positive.")
        self._instance_data[instance] = value

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")



class Planet:
    def __init__(
        self,
        name,
        radius_metres,
        mass_kilograms,
        orbital_period_seconds,
        surface_temperature_kelvin,
    ):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty name")
        self._name = value

    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()


pluto = Planet(
    name="Pluto",
    radius_metres=1184e3,
    mass_kilograms=1.305e22,
    orbital_period_seconds=7816012992,
    surface_temperature_kelvin=55,
)

print(pluto.radius_metres)
print(Positive.__get__(Planet.__dict__["radius_metres"], pluto, Planet))

