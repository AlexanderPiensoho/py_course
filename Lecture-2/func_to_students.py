#Den här funktionen anropas och visar menyn
def show_menu():
    print("\nGör ett av följande menyval:\n".upper())
    print("Menyval 1 - lägg till student".upper())
    print("Menyval 2 - Ta bort en student".upper())
    print("Menyval 3 - lista över studenter".upper())
    print("Menyval 4 - Sök student".upper())
    print("Menyval 5 - Räkna genomsnittlig ålder".upper())
    print("Menyval 6 - avsluta".upper())
    

# Den här funktionen hanterar menyval
def menu_choice_func(menu_choice_number, menu_choice_string):
    choice_is_valid = int(menu_choice_number) in [1,2,3,4,5,6]
    if not choice_is_valid:
        print("felaktigt val")
    print(f"Du har valt: {menu_choice_number}{menu_choice_string}")
    