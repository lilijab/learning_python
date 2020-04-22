class Chicken:
    total_eggs = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
        return self.eggs


chicken1 = Chicken('chicken', "CoCo")
print(chicken1.species, chicken1.name, chicken1.eggs)
print(Chicken.total_eggs)
chicken1.lay_egg()
print(chicken1.eggs)
print(Chicken.total_eggs)