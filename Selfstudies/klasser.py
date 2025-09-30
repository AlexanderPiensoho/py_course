class Car:

    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def drive(self):
        print(self.brand + ": Kör framåt")   

    def honk(self):
        print(self.brand + ": Tut tut!")

    def breaking(self):
        print(self.brand + ": Bromsar...")

volvo = Car("Volvo", 2018, "Vit")

volvo.drive()
volvo.honk()
volvo.breaking()