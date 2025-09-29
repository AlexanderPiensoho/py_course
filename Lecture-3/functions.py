'''
Förstå varför funktioner används.

känna till syntaxen
'''
#I defenitionen kallar vi det parameter
#Defenition av funktionen
def say_hello(user_name, extra_message=""):
    print(f"Hej {user_name} - {extra_message}")
    name_length = len(user_name)
    return name_length # retunerar ett värde - t.ex. en beräkning - vi måste ta emot returnen senare

name = input("Your name: ")
#Anropar funktionen - när vi anropar funktionen kallar vi det argument och INTE parameter
len1 = say_hello(name, "Du suger!")
print(f"Length of {name} is {len1}\n")

len2 = say_hello("Chrille", "Du tror du är cool")
print(f"Length of Chrille is {len2}\n")

len3 = say_hello("Elin")
print(f"Length of Elin is {len3}\n")

def f(x):
    y = x + 1
    return y
def square(x):
    y = x * x
    return y

print(square(2))
print(square(3))
print(square(4))
