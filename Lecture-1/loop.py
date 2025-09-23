app_is_running = True

while app_is_running == True:
    print("Menyval 1")
    print("Menyval 2")
    print("Menyval 3")
    print("Avsluta 4")
    menu_choice = input("Vilken Meny? ")

    if(menu_choice == "1"):
        print("Välkommen till meny 1")
    elif(menu_choice == "2"):
        print("välkommen till meny 2")
    elif(menu_choice == "3"):
        print("välkommen till meny 3")
    elif(menu_choice == "4"):
        print("Programmet avslutat")
        app_is_running = False
    else:
        print("Okänt val, försök igen")


animal_list = ["hund", "katt", "fisk", "häst"]

for animal in animal_list:
    print(animal)
    if animal == "hund":
        print("Woof!")
    else:
        print("noob!")

print()

for i in range(len(animal_list)):
    print(animal_list[i])

for i in range(10):
    print("1337")