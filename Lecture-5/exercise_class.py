class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed
    
    def __str__(self):
        return f"Brand: {self.brand} | Speed: {self.speed}"
    
    def accelerate(self):
        self.speed += 10
        return self.speed

    def brake(self):
        if self.speed <= 0:
            return 0
        else:
            self.speed -= 10
            return self.speed

    def current_speed(new_speed):
        pass

        

volvo = Car("Volvo V70", 0)
audi = Car("Audi RS6", 0)

volvo.accelerate()
volvo.accelerate()
print(volvo.speed)

print(volvo)
