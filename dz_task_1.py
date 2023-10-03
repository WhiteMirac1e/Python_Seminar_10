class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None
    def get_spec(self):
        return self.spec

class Fish(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec

class Birds(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
    
class Snakes(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec      

f1 = Fish("Frik", 4, "Swim")
b1 = Birds("Chik", 3, "Fly")
s1 = Snakes("Kobra", 15, "SHHH")

# for pet in [f1, b1, s1]:
#     print(pet.get_spec())

class Fabric:
    def create_animal(self, animal_type, *args, **kwargs):
        new_animal = self.get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def get_maker(self, animal_type):
        types = {"fish": Fish, "birds": Birds, "snakes": Snakes}
        return types[animal_type.lower()]
    
fab = Fabric()
animal_from_fabric = fab.create_animal('birds', "Frik", 5, "Swim")
