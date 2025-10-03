''' Just me trying to make sense of functions without destroying any of my regular programs'''


alarms = {
    "cpu": [2, 10, 40],
    "memory": [2,30, 40],
    "disk": [2]
}

def press_enter_to_continue ():
   input("Tryck enter för att fortsätta...".upper())


def show_alarm_menu():
        print("\nKonfigurera larm\n".upper())
        print("1. CPU användning")
        print("2. Minnesanvändning")
        print("3. Diskanvändning")
        print("4. Tillbaka till huvudmenyn")

def set_alarm_choice(): #Hanterar användarens menyval för alarm menyn
    while True:
        alarm_menu_choice = input("Gör ett val mellan 1-4: ")
        try:
            choice_number = int(alarm_menu_choice)
            if 1<= choice_number <=4:
                return alarm_menu_choice
            else:
                print("välj en siffra mellan 1-4")
        except ValueError:
            print("Det måste vara en siffra")

def set_alarm(alarm_type, input_message):
    while True:
        try:
            alarm_value = int(input(input_message))
            if 0<= alarm_value <=100:
                alarms[alarm_type].append(alarm_value)
                print(f"\nDitt {alarm_type} alarm är inställt på {alarm_value}%".upper())
                press_enter_to_continue()
                break
            else:
                print("Siffran måste vara mellan 0-100")
        except ValueError: 
            print("Felaktigt värde, det måste vara en siffra mellan 0-100")


def handle_alarm_menu():
    menu_running = True
    alarm_config = {
        "1": ("cpu", "set CPU alarm (0-100): "),
        "2": ("memory", "set RAM alarm (0-100): "),
        "3": ("disk", "set DISK alarm (0-100): ")
    }

    while menu_running:
        show_alarm_menu()
        choice = set_alarm_choice()
        if choice in alarm_config:
            alarm_type, prompt = alarm_config[choice]
            set_alarm(alarm_type, prompt) 
            print(f"You selected: {alarm_type}")
        elif choice == "4":
            break


handle_alarm_menu()



