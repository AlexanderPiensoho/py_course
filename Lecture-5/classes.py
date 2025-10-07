class Person():
    def __init__(self, name_str, age):#__init__ är en konstuktor. Den körs en gång varje ett nytt objekt startar
        self.name = name_str
        self.age = age
    
    def __str__(self): #Viktigt med return. Så vi faktiskt retunernar att det ska bli en sträng.
        return f"Namn: {self.name} | Ålder: {self.age}"

    def greet(self, name_to_greet=None):
        if name_to_greet:
            print(f"Hej {name_to_greet}, jag heter {self.name} och är {self.age} år gammal.")
        else:
            print(f"Hej, jag heter {self.name} och är {self.age} år gammal")

    def change_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name
    
#anropar klassen från kanske en annan fil

p1 = Person("Ada", 25) #Det första som händer är att körs __init__, det är därför vi kallar det med Person (klassnamnet)
p2 = Person("Bob", 30)
p3 = Person("Karin", 45)
p4 = Person("David", 20)

p1.greet()
p2.greet("Ada")
p3.greet("Bob")
p4.greet("Karin")

# Vi vill helst inte ge direktåtkomster till atribut i klasserna i den globala programmet. därför är det bättre med fler metoder i klassen
new_name = input(f"Ange ny namne för användern {p1.get_name()}: ")
p1.change_name(new_name)
print(f"Nytt namn för användare: ",p1.get_name())
print()
print(p1)
print()
my_list = [p1, p2, p3, p4]
for i in range(len(my_list)):
    print(my_list[i])
print()
for person in my_list:
    print(person)

for i in range(len(my_list)):
    print(f"person # {i+1}, {my_list[i]}")