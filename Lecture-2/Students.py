from func_to_students import show_menu, menu_choice_func


student_list =[]
menu_is_running = True
while menu_is_running:
    print("\n==HEJ OCH VÄLKOMMEN TILL STUDENTMENYN==")
    show_menu()

    menu_choice = input("Gör ett val mellan 1-5: ".upper())
    if menu_choice == "1":
        menu_choice_func(menu_choice,": Lägg till student\n")
        student_name = input("Vad är studentens namn? ")
        student_age = input("Vad är studentens ålder? ")
        student_info = {
            "namn" : student_name,
            "ålder" : student_age
        }
        student_list.append(student_info)
        
        #print(student_info)

    elif menu_choice == "2":
        menu_choice_func(menu_choice,": Lista över studenter")
        print(student_list)

    elif menu_choice == "3":
        menu_choice_func(menu_choice,": Sök student")
        search_student = input ("\nSök efter student, skriv ett förnamn: ")

        for student in student_list:
            if student["namn"] == search_student:
                print(f"Student {student} finns i listan")

    elif menu_choice == "4":
        menu_choice_func(menu_choice,": Räkna genomsnitlig ålder")
        total_age = 0
        for student in student_list:
            total_age = total_age + int(student["ålder"])
        avarage = total_age / len(student_list)
        print(f"Genomsnittsåldern är {avarage}")

    elif menu_choice == "5":
        menu_choice_func(menu_choice,": Avsluta")
        print("\n==AVSLUTAR PROGRAMMET==\n")
        break

    else: 
        print("Gör ett val mellan 1-5")
    