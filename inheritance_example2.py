class Magari:
    def __init__(self, make, model, year):
        self.mymake = make
        self.mymodel = model
        self.myyear = year

    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} started")

class Toyota(Magari):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.mynum_doors = num_doors

    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} car with {self.mynum_doors} doors started")

gari = Toyota("Premio", "Saloon", 2023, 5)
gari.kuanzisha()

class Motorcycle(Magari):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.myengine_size = engine_size


    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} made in {self.myyear} engine is {self.myengine_size} cc")

vroom = Motorcycle("Honda", "Cruiser", 2020, 500)
vroom.kuanzisha()