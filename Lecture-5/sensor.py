import random

class Sensor:
    def __init__(self, type, level):
        self.type = type
        self.level = level

    def __str__(self):
        return f"{self.type} | {self.level}"
    
    #Läser in värdet just nu med random, en int mellan 1, 100. 
    def read(self):
        self.level = random.randint(1, 100)
        return self.level
    
    #Läser av om värdet (threshold ex 70) är högre eller lägre än värdet just nu.
    def is_alarm_triggered(self, threshold):
        if self.level > threshold:
            return True
        else:
            return False

cpu = Sensor("CPU", 50)
ram = Sensor("RAM-minne", 40)

print(cpu.read())
print(cpu.is_alarm_triggered(60))
