from func_to_students import show_menu, menu_choice_func

student_list =[]
menu_is_running = True
while menu_is_running:
    print("\n==HEJ OCH VÄLKOMMEN TILL STUDENTMENYN==")
    show_menu()

    menu_choice = input("\nGör ett val mellan 1-6: ".upper())
    if menu_choice == "1":
        menu_choice_func(menu_choice,": Lägg till student\n")
        student_name = input("Vad är studentens namn? ")
    
        while True:
            student_age = input("Vad är studentens ålder? ")
            try:
                age_number = int(student_age)
                if age_number < 0 or age_number > 120:
                    print("Felaktigt val: Välj en siffra mellan 0-120")
                    continue
                else:
                    break
            except ValueError:
                print("Ålder måste vara en siffra")
                continue
        student_favorite = input("Vad är studentens favoritämne: ")
        student_info = {"namn" : student_name, 
                        "ålder" : student_age,
                        "favoritämne" : student_favorite
                        }
        student_list.append(student_info)
            
    elif menu_choice == "2":
        menu_choice_func(menu_choice,": Ta bort en student")
        remove_student = input ("Skriv namnet på studenten du vill ta bort: ")

        found = False
        for student in student_list:
            if student["namn"].lower() == remove_student.lower():
                student_list.remove(student)
                print(f"Studenten {student} har tagits bort från listan")
                found = True
                break
        if not found:
                print("Ingen med det namnet hittades!")

    elif menu_choice == "3":
        menu_choice_func(menu_choice,": Lista över studenter")
        if len(student_list) == 0:
            print("Inga studenter är listade än!")
        else:
            print("===LISTA ÖVER ALLA STUDENTER===")
            for student in student_list:
                print(f"Namn: {student["namn"]} -- Ålder: {student["ålder"]} år -- Favoritämne: {student["favoritämne"]}")
            print("==============================")
        input ("Tryck Enter för att komma tillbaka till menyn...")

    elif menu_choice == "4":
        menu_choice_func(menu_choice,": Sök student")
        search_student = input ("\nSök efter student, skriv ett förnamn: ")

        for student in student_list:
            if student["namn"].lower() == search_student.lower():
                print(f"Student {student} finns i listan")
                break
            else:
                print(f"{search_student} finns inte i listan")

    elif menu_choice == "5":
        menu_choice_func(menu_choice,": Räkna genomsnitlig ålder")
        total_age = 0    
        if len(student_list) == 0:
            print("\nInga studenter är registrerade än!".upper())
            
        for student in student_list:
            total_age = total_age + int(student["ålder"])
        avarage = total_age / len(student_list)
        print(f"Genomsnittsåldern är {avarage}".upper())
        input("Tryck Enter för att komma tillbaka till menyn...")
                    

    elif menu_choice == "6":
        menu_choice_func(menu_choice,": Avsluta")
        print("\n==AVSLUTAR PROGRAMMET==\n")
        break

    else: 
        print("Gör ett val mellan 1-6")
    