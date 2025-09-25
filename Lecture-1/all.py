'''
Bygg ett litet program som:
1. Frågar användaren efter namn, ålder och favoritfärg.
2. Sparar informationen i en dictionary.
3. Lägger till användarens favoritfilmer i en lista.
4. Skriver ut en personlig hälsning och sammanfattning av informationen.
5. Om användaren är under 18, skriv en extra rad: "Du är minderårig."
'''

print("\n==Hej och välkommen till världens coolaste program!==\n".upper())
user = {
    "Namn": "",
    "Ålder": "",
    "Favoritfärg": "",
}


user["Namn"] = input("Ange ditt fullständinga namn: ")
user["Ålder"] = input("Ange din ålder: ")
user["Favoritfärg"] = input("Ange din favoritfärg: ")

#for key, value in user.items():
 #   print(f"{key}: {value}")

film = []
add_film = input("Skriv din favoritfilm: ")
film.append(add_film)

print(f"Hej {user["Namn"]}! Du är {user["Ålder"]} år gammal och din favoritfärg är {user["Favoritfärg"]}.")
for i in film[::1]:
    print(f"Din favoritfilm är: {i}")

if int(user["Ålder"]) < 18:
    print("Du är minderårig")


